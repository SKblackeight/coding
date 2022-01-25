from PIL.ExifTags import TAGS
from PIL import Image

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val
    return labeled

exif = get_exif('cute.jpg')
labeled = get_labeled_exif(exif)
print(labeled)
print(labeled['DateTimeOriginal'])