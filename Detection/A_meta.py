from PIL import Image
from PIL.ExifTags import TAGS


def header_write(path, expiration):
    img = Image.open(path)
    if (img.format == "JPEG"):
        jpg_wr_meta(img,expiration)

    img.close()

def jpg_wr_meta(jpg, exDate):
    
    meta_data = jpg.getexif()
    meta_data[0x9286] = exDate
    jpg.save(jpg.filename, exif = meta_data)