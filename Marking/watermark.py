# pip3 install opencv-python qrcode numpy
import numpy as np
import cv2
import qrcode

def put_text():
    # Create a black image
    img = np.zeros((512,512,3), np.uint8)

    # Write some Text
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = [(10,500),(110,450),(210,400),(310,350),(10,300),(110,250),(210,200),(310,150),(10,100),(110,50)]
    fontScale              = 1
    fontColor              = (1,1,1)
    thickness              = 1
    lineType               = 2

    for text in bottomLeftCornerOfText:
        cv2.putText(img,'Hello World!', text, font, fontScale, fontColor, thickness, lineType)

    #Save the image
    cv2.imwrite("out.jpg", img)

def qr_img(code):
    qr = qrcode.QRCode()
    qr.add_data(code)
    qr.make()
    img = qr.make_image(fill_color="white", back_color="black")
    return img

def img_add(src1, src2):
    alpha = 0.99
    beta = 0.01
    gamma = 0

    dst = cv2.resize(src2, dsize=(src1.shape[1],src1.shape[0]))
    return cv2.addWeighted(src1, alpha, dst, beta, gamma)

def img_diff(src1, src2):
    return cv2.subtract(src1, src2)

def img_add2(img):
    src1 = img
    src2 = img
    for i in range(0,253):
        src2 = cv2.add(src1, src2)
    cv2.imwrite("out.jpg",src2)
    
if __name__ == "__main__":
    img_1 = cv2.imread("test2.jpg")
    img_QR = qr_img("갓기웅")
    img_2 = cv2.cvtColor(np.array(img_QR), cv2.COLOR_RGB2BGR)
    cv2.imwrite("output.jpg", img_2)
    img_out = img_add(img_1, img_2)
    cv2.imwrite("img.jpg", img_out)
    img_add2(img_diff(img_1, img_out))