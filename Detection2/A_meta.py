## jpg_info 함수에서 return값 대신 jpg.delete를 수정하는것으로 변경

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
                    if jpg.metadata < float(time.time()-604800):
                        jpg.delete = True
                else:
                    jpg.confirmed = False
            except:
                raise Exception('[Image File Error] Can not check Image metadata')