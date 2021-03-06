import cv2
import numpy as np

def detecter(path) -> bool:
    img = cv2.imread(path)
    img = cv2.resize(img, None, fx=0.6, fy=0.6)
    height, width, channels = img.shape

    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
            
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                    
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            return True
    return False

net = cv2.dnn.readNet("yolov4-ANPR.weights", "yolov4-ANPR.cfg") #다운받아야됨
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

if __name__ == "__main__":
    iscar = []
    files = ["car1.jpg","test1.jpg","car2.jpg","test2.jpg","car3.jpg","test3.jpeg","car4.jpeg","test4.jpeg","car5.jpg","car6.jpg","car7.jpeg","car8.JPG","car9.JPEG"]
    for f in files:
        if detecter(f):
            iscar.append(f)
    print (iscar)