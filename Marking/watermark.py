import cv2

# def put_text():
#     print("test")
#     putText()

def img_add(img_1, img_2):
    src1 = cv2.imread(img_1)
    src2 = cv2.imread(img_2)
    alpha = 0.5
    beta = 0.5
    gamma = -1
    cv2.imwrite("out.jpg", cv2.addWeighted(src1, alpha, src2, beta, gamma))

def img_diff(img_1, img_2):
    src1 = cv2.imread(img_1)
    src2 = cv2.imread(img_2)

    cv2.imwrite("out.jpg",cv2.subtract(src1, src2))

if __name__ == "__main__":
  img_diff("real.jpg", "tester.jpg")
