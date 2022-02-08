from PIL import Image
from PIL.ExifTags import TAGS
from PIL.PngImagePlugin import PngImageFile, PngInfo
# import time
import os

def header_check(path):
    img_ck = []

    img = Image.open(path)
    if (img.format == "JPEG"):
        img_ck.append(jpg_info(img))
    # elif (img.format == "PNG"):
    #     img_ck.append(png_info(img))
    else:
        img_ck.append(None)
    img.close()
    for i in img_ck:
        print (i)


def jpg_info(jpg):
    meta_data = jpg.getexif()
    tag_label = {}
    for tag, value in meta_data.items():
        decoded = TAGS.get(tag,tag)
        tag_label[decoded] = value
    try:
        if "UserComment" in tag_label.keys():
            return str(tag_label["UserComment"])
        else:
            return None
    except:
        return None

def header_write(path, expiration):
        
    img = Image.open(path)
    if (img.format == "JPEG"):
        jpg_wr_meta(img,expiration)

    img.close()

def jpg_wr_meta(jpg, exDate):
    
    meta_data = jpg.getexif()
    meta_data[0x9286] = exDate
    jpg.save(jpg.filename, exif = meta_data)

if __name__ == "__main__":
    
    directory = 'address'

    for i in os.listdir(directory):
        path = directory+i
        header_write(path, "2022:11:21 18:18:18")

    for i in os.listdir(directory):
        path = directory+i
        header_check(path)

