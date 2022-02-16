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
    img = qr.make_image(fill_color="black", back_color="#FFFFFF")
    return img

def img_add(src1, src2):
    src1_width = src1.shape[0]
    src1_height = src1.shape[1]
    src1 = cv2.subtract(src1,5*np.ones((src1_width,src1_height,3), np.uint8))
    src2 = cv2.resize(src2, dsize=(src1_height,src1_width))
    return cv2.add(src1, src2)

def img_diff(src1, src2):
    src2 = cv2.add(src2, 2*np.ones((src1.shape[0],src1.shape[1],3), np.uint8))
    src1 = cv2.subtract(src2, src1)
    for i in range(0,8):
        src1 = cv2.add(src1, src1)
    cv2.imwrite("diff.jpg", src1)

def img_tile(img_list):
    img = cv2.vconcat([cv2.hconcat(img) for img in img_list])
    return img
    
if __name__ == "__main__":
    print("Read 'cute.jpg' file")
    img_1 = cv2.imread("cute.jpg")
    # img_out = cv2.imread("QR_test1.jpg")
    img_QR = qr_img("송유정 바보")
    img_2 = cv2.cvtColor(np.array(img_QR), cv2.COLOR_RGB2BGR)
    img_tile_res = img_tile( [[ img_2, img_2 ], [ img_2, img_2 ]] )
    cv2.imwrite("QR.jpg", img_tile_res)
    img_out = img_add(img_1, img_tile_res)
    print("write 'edited.jpg' file")
    cv2.imwrite("edited.jpg", img_out)

    print("Read 'cute.jpg' file")
    img_1 = cv2.imread("cute.jpg")
    print("write 'edited.jpg' file")
    img_out = cv2.imread("edited.jpg")
    img_diff(img_1, img_out)