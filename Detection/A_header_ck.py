import os, shutil
import time
import PIL.Image
from PIL.ExifTags import TAGS
from tkinter import *

def header_check(filedir):
    
    img_ck = []
    img = PIL.Image.open(filedir)

    if (img.format == "JPEG"):
        img_ck.append(jpg_info(img))

    else:
        pass
    img.close()


    for i in img_ck:
        # print (i)
        current_date = float(time.time())
        date = (current_date - i)
        # print(date)
        if date > 400000 :
            print (filedir)
            # os.remove(path+'\\'+filename+fileExtension)  #삭제
        else :
            pass

def header_check2(filedir):
    img_ck = []
    img = PIL.Image.open(filedir)

    if (img.format == "JPEG"):
        img_ck.append(jpg_info(img))

    else:
        pass
    img.close()


    for i in img_ck:
        # print (i)
        current_date = float(time.time())
        date = (current_date - i)
        # print(date)
 
        if date < 4000000:
            return(filedir)
            # os.remove(path+'\\'+filename+fileExtension)  #삭제
            

def jpg_info(jpg): 
    meta_data = jpg.getexif()
    tag_label = {}
    for tag, value in meta_data.items():
        decoded = TAGS.get(tag,tag)
        tag_label[decoded] = value
    try:
        if "UserComment" in tag_label.keys():
            return (float(tag_label["UserComment"]))
        else:
            return 0
    except:
        return 0

