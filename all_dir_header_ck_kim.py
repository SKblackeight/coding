from PIL import Image
from PIL.ExifTags import TAGS
import os, time


def header_check(buf):
    img_ck = []

    img = Image.open(buf)
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
            return float(tag_label["UserComment"])
        
        else:
            return None
    except:
        return None


def header_write(buf, expiration):
        
    img = Image.open(buf)
    if (img.format == "JPEG"):
        jpg_wr_meta(img,expiration)
    # elif (img.format == "PNG"):
    #     png_wr_meta(img, expiration)
    img.close()

def jpg_wr_meta(jpg, exDate):
   
    
    meta_data = jpg.getexif()
    meta_data[0x9286] = exDate
    jpg.save(jpg.filename, exif = meta_data)


if __name__ == "__main__":
   
    directory = ("address")

    for path, dirs, files in os.walk(directory):
        for names in files:
            filedir = os.path.join(path,names)
            
            afile = open(filedir, 'rb')
            time1 = float(time.time())
            header_write(filedir, time1)

    for path, dirs, files in os.walk(directory):
        for names in files:
            filedir = os.path.join(path,names)
            afile = open(filedir, 'rb')
            header_check(afile)
