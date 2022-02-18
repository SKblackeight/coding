## filedir -> filedir.path로 수정
## return 부분을 없애고 file.plate 수정

from PIL import Image
from PIL.ExifTags import TAGS
from PIL.PngImagePlugin import PngImageFile, PngInfo
import numpy as np
import cv2

def detect_car(filedir):
    net = cv2.dnn.readNet("yolov4-ANPR.weights", "yolov4-ANPR.cfg")
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]

    img = cv2.imread(filedir.path)
    img = cv2.resize(img, None, fx=0.5, fy=0.5)

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
            if confidence > 0.95:
                # Object detected
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

    for i in range(len(boxes)):
        if i in indexes:
            label = str(classes[class_ids[i]])
            if 'licence_plate' == label:
                filedir.plate = True
                filedir.delete = True
