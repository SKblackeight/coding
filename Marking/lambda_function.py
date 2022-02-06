import numpy as np
import cv2
import qrcode
import boto3
import uuid
from urllib.parse import urlparse
import io
import requests
import base64

def qr_img(path, code):
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

def lambda_handler(event, context=None):
    get_context = event["getObjectContext"]
    route = get_context["outputRoute"]
    token = get_context["outputToken"]
    s3_url = get_context["inputS3Url"]

    # Transform object
    image_request = requests.get(s3_url)
    key = s3_url.split('?')[0].split('/')[-1]
    img1_path = "/tmp/{}{}".format(uuid.uuid4(), key)
    with open(img1_path, "wb") as img1:
        img1.write(image_request.content)
    img2_path = "/tmp/{}.png".format(uuid.uuid4())
    qr_img(img2_path, "test")


    cv2.imwrite(img1_path, img_add(img1_path, img2_path))
    with io.open(img1_path, "rb") as transformed:

        # Write object back to S3 Object Lambda
        s3 = boto3.client("s3")
        s3.write_get_object_response(Body=transformed.read(),RequestRoute=route,RequestToken=token)

    # Exit the Lambda function: return the status code  
    return {"status_code": 200}

    # img3 = (img_add(img1_path, img2_path))
    # s3 = boto3.client("s3")
    # s3.write_get_object_response(Body=img3,RequestRoute=route,RequestToken=token)
    # return {"status_code": 200}