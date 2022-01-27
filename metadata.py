# pip3 install Pillow

from PIL import Image
from PIL.ExifTags import TAGS
from PIL.PngImagePlugin import PngImageFile, PngInfo
# import time

def header_check(img_files):
    img_ck = []
    for img_file in img_files:
        img = Image.open(img_file)
        if (img.format == "JPEG"):
            img_ck.append(jpg_info(img))
        elif (img.format == "PNG"):
            img_ck.append(png_info(img))
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

def png_info(png):
    try:
        if "UserComment" in png.text.keys():
            return str(png.text["UserComment"])
        else:
            return None
    except:
        return None

def header_write(img_files, expiration):
    for img_file in img_files:
        img = Image.open(img_file)
        if (img.format == "JPEG"):
            jpg_wr_meta(img, expiration)
        elif (img.format == "PNG"):
            png_wr_meta(img, expiration)
        img.close()

def jpg_wr_meta(jpg, exDate):
    meta_data = jpg.getexif()
    meta_data[0x9286] = exDate
    jpg.save("out.jpg", exif = meta_data)

def png_wr_meta(png, exDate):
    meta_data = PngInfo()
    meta_data.add_text("UserComment", exDate)
    png.save("out.png", pnginfo = meta_data)

# t = img_info()
# time_stamp = int(time.mktime(time.strptime(t, "%Y:%m:%d %H:%M:%S")))
# nowdate = int(time.time())
# print(time_stamp)
# print(nowdate)
# if (time_stamp<nowdate):
#     print("FALSE")

if __name__ == "__main__":
    # image_files = ["test1.jpg", "test2.jpg", "test3.jpeg", "test4.jpeg", "test5.png", "test6.png"]
    image_files = ["in.jpg", "in.png"]
    header_write(image_files, "2022:11:21 18:18:18")
    image_files = ["out.jpg", "out.png"]
    header_check(image_files)