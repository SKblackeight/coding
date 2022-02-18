from PIL import Image
from PIL.ExifTags import TAGS
import numpy as np
import os,cv2
from pydantic import BaseModel

def detect_car(filedir):
    net = cv2.dnn.readNet("yolov4-ANPR.weights", "yolov4-ANPR.cfg")

    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i- 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    img = cv2.imread(filedir)
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
                    
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            # x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            # color = colors[i]
            # cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            # cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
        

            if label == 'licence_plate':
            # filedir.close()
            # os.remove(filedir) #제거
                print (filedir)
                # file_destination = ''
                # shutil.move(filedir, file_destination)  #이동       
            else:
                continue

    # cv2.imshow("Image", img)
    # cv2.waitKey()  

    # cv2.destroyAllWindows()

class File(BaseModel):
    path : str
    header : str
    hash : str
    confirmed : bool
    metadata : float
    is_car : bool
    delete : bool

if __name__ == "__main__":
    dic_dir ='Detection/SKB'
    file_list=[]

    # make file_list
    for path, dir, files in os.walk(dic_dir):
        for name in files:
            file_path = os.path.join(path,name)
            file_list.append(File(path=file_path, header="", hash=False, confirmed=False, metadata=0.0, is_car=False,delete=False))
    for file in file_list:
        detect_car(file.path)