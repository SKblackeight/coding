from PIL import Image
from PIL.ExifTags import TAGS
import time

def jpg_info(jpg):
    with Image.open(jpg.path) as img:
        if (img.format == "JPEG"):
            meta_data = img.getexif()
            tag_label = {}
            for tag, value in meta_data.items():
                decoded = TAGS.get(tag,tag)
                tag_label[decoded] = value
            try:
                if "UserComment" in tag_label.keys():
                    jpg.metadata = tag_label["UserComment"]
            except:
                raise Exception('[Image File Error] Can not check Image metadata')
            if jpg.metadata < float(time.time()-604800):
                jpg.delete = True