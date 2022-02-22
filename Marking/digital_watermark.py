# 수정이 가해지면 워터마크를 잘 못찾음

# pip3 install invisible-watermark

import cv2
from imwatermark import WatermarkEncoder, WatermarkDecoder
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

def embed(img, wm):
    bgr = cv2.imread(img)

    encoder = WatermarkEncoder()
    encoder.set_watermark('bytes', wm.encode('utf-16'))
    bgr_encoded = encoder.encode(bgr, 'dwtDctSvd')

    cv2.imwrite('in.jpg', bgr_encoded)

def decode(img):
    bgr = cv2.imread(img)

    decoder = WatermarkDecoder('bytes', 32)
    watermark = decoder.decode(bgr, 'dwtDctSvd')
    # watermark = decoder.decode(bgr, 'rivaGan')
    

    print(watermark.decode('utf-16'))

if __name__ == "__main__":
    WatermarkEncoder.loadModel()
    image_file = "a.png"
    embed(image_file, "te")
    image_file = "in.jpg"
    decode(image_file)
    