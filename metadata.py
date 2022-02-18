from email import header
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.PngImagePlugin import PngImageFile, PngInfo
import os
import time

def header_check(path):
    with Image.open(path["name"]) as img:
        if (img.format == "JPEG"):
            path["header"] = "JPEG"
            path["metadata"] = jpg_info(img)
        # elif (img.format == "PNG"):
        #     img_ck.append(png_info(img))
        else:
            path["header"] = "other"

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

def header_write(img_file, expiration): 
    img = Image.open(img_file["name"])
    if (img.format == "JPEG"):
        jpg_wr_meta(img,expiration)
    img.close()

def jpg_wr_meta(jpg, exDate):
    meta_data = jpg.getexif()
    meta_data[0x9286] = exDate
    jpg.save(jpg.filename, exif = meta_data)

if __name__ == "__main__":
    directory = './temp/'
    path = []
    for i in os.listdir(directory):
        path.append({"name":directory+i, "header":None, "metadata":None, "hash":None})
    # print(path)
    for file_ck in path:
        # print(file_ck["name"])
        header_write(file_ck, float(time.time() - 604800))