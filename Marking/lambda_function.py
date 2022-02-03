import numpy as np
import cv2
import qrcode
import boto3
import sys
import uuid
from urllib.parse import unquote_plus
import json
import base64

s3_client = boto3.client('s3')

def qr_img(code, path):
    qr = qrcode.QRCode()
    qr.add_data(code)
    qr.make()
    img = qr.make_image(fill_color="white", back_color="black")
    img.save(path)

def img_add(path1, path2):
    src1 = cv2.imread(path1)
    src2 = cv2.imread(path2)
    alpha = 0.99
    beta = 0.01
    gamma = 0
    src1_width = np.array(src1).shape[0]
    src1_height = np.array(src1).shape[1]
    dst = cv2.resize(src2, dsize=(src1_height,src1_width))
    return cv2.addWeighted(src1, alpha, dst, beta, gamma)

def img_diff(src1, src2):
    return cv2.subtract(src1, src2)

# def resize_image(image_path, resized_path):
#   with Image.open(image_path) as image:
#       image.thumbnail(tuple(x / 2 for x in image.size))
#       image.save(resized_path)

def lambda_handler(event, context=None):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        tmpkey = key.strip('/')[-1:]
        img1_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
        print(img1_path)
        img2_path = '/tmp/qr.png'
        s3_client.download_file(bucket, key, img1_path)

        qr_img("송유정 바보", img2_path)
        mk_img = img_add(img1_path, img2_path)
        b64_str = base64.b64encode(mk_img)

    # Exit the Lambda function: return the status code  
    return {
        'status_code': 200,
        'header' : {
            'Content-Length' : json.dumps(sys.getsizeof(b64_str)),
            'Content-Type' : "image/jpeg",
            'Content-Disposition' : json.dumps("attachment;filename={}".format(uuid.uuid4())),
        },
        'isBase64Encoded' : True,
        'body': json.dumps(b64_str.decode('utf-8'))
    }