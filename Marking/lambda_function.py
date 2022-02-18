import numpy as np
import cv2, qrcode
from PIL import Image
from PIL.ExifTags import TAGS
import boto3
from urllib.parse import unquote_plus
import pymysql
import json
import os, sys, logging
import uuid, base64, time
import hashlib

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def qr_img(code):
    qr = qrcode.QRCode()
    qr.add_data(code)
    qr.make()
    return qr.make_image(fill_color='black', back_color='#020202')

def img_add(src1, src2):
    src1_width = src1.shape[0]
    src1_height = src1.shape[1]
    src1 = cv2.subtract(src1,2*np.ones((src1_width,src1_height,3), np.uint8))
    src2 = cv2.resize(src2, dsize=(src1_height,src1_width))
    return cv2.add(src1, src2)

def rds_config():
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']

    os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'
    try:
        logger.info('Connecting to Database...')
        return pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASS, port=int(DB_PORT), database=DB_NAME, connect_timeout=5)
    except Exception as e:
        logger.error('Database connection failed due to {}'.format(e))
        raise Exception('[InternalServerError] Can not acccess rec db')

def jpg_wr_meta(jpg, path, exDate):
    meta_data = jpg.getexif()
    meta_data[0x9286] = exDate
    jpg.save(path, exif = meta_data)

def hashing(hfile):
    hash = hashlib.sha256()
    hash.update(hfile)
    return hash.hexdigest()

def lambda_handler(event, context):
    S3_BUCKET = os.environ['S3_BUCKET']
    KEY = unquote_plus(event['key'])
    USER = unquote_plus(event['user'])
    TMPKEY = KEY.strip('/')[-1]
    CODE = USER + '-' + str(uuid.uuid4())

    try:
        s3_client = boto3.client('s3')
        img1_path = '/tmp/{}.jpg'.format(uuid.uuid4(), TMPKEY)
        with open(img1_path, 'w+b') as img1:
            s3_client.download_fileobj(S3_BUCKET, KEY, img1)
    except Exception as e:
        logger.error('S3 connection failed due to {}'.format(e))
        raise Exception('[BadRequest] Can not found S3 object')

    img_1 = cv2.imread(img1_path)
    img_2 = cv2.cvtColor(np.array(qr_img(CODE)), cv2.COLOR_RGB2BGR)
    npimg = cv2.cvtColor(img_add(img_1, img_2), cv2.COLOR_BGR2RGB)
    jpg_wr_meta(Image.fromarray(npimg),img1_path, time.time())
    
    with open(img1_path, 'rb') as img1:
        buf = img1.read()
        hash = hashing(buf)
        b64_str = base64.b64encode(buf)

    rds = rds_config()
    if rds:
        with rds.cursor() as cursor:
            query = 'INSERT INTO rec VALUES(%s,%s)'
            cursor.execute(query,(hash,CODE))
            logger.info('excuted')
            rds.commit()

        # Exit the Lambda function: return the status code  
        return {
            'statusCode': '200',
            'headers' : {
                'Timestamp' : time.time(),
                'Content-Length' : json.dumps(sys.getsizeof(b64_str)),
                'Content-Type' : 'image/jpeg',
                'Content-Disposition' : json.dumps('attachment;filename={}'.format(uuid.uuid4())),
            },
            'isBase64Encoded': True,
            'body': b64_str.decode('utf-8')
        }
    else:
        raise Exception('[InternalServerError] Can not acccess rec db')

    # img3 = (img_add(img1_path, img2_path))
    # s3 = boto3.client('s3')
    # s3.write_get_object_response(Body=img3,RequestRoute=route,RequestToken=token)
    # return {'status_code': 200}