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
            return meta_date(float(tag_label["UserComment"]))
        else:
            return None
    except:
        return None


def meta_date(previous_date):
    current_date = time.time()
    date = (current_date - previous_date)
    if date > 604800:
        return False
    else :
        return True

def header_write(path, expiration):
    img = Image.open(path)
    if (img.format == "JPEG"):
        jpg_wr_meta(img,expiration)

    img.close()

def jpg_wr_meta(jpg, exDate):
    
    meta_data = jpg.getexif()
    meta_data[0x9286] = exDate
    jpg.save(jpg.filename, exif = meta_data)

def mkdir_list(directory):
    list_dir = []
    for path, dir, files in os.walk(directory):
        for f in files:
            list_dir.append({"name":path+"/"+f, "header":None, "metadata":None, "hash":None})
    return list_dir

if __name__ == "__main__":
    list_dir = mkdir_list("./dataset/")
    for file_ck in list_dir:
        header_check(file_ck)
        if file_ck["header"] == "JPEG":
            meta_date(file_ck["metadata"])
        print(file_ck)

    # for file_ck in path:
    #     if not(file_ck["metadata"]):
    #         os.remove(file_ck["name"])
