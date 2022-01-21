from PIL import Image
from PIL.ExifTags import TAGS
from sklearn.feature_extraction import image
from datetime import date
import time
from PIL.JpegImagePlugin import JpegImageFile

def img_info():
    img = Image.open('cute.jpg')
    meta_data = img._getexif()
    img.close()

    taglabel = {}
    #o = meta_data.items()
    for tag, value in meta_data.items():
        decoded = TAGS.get(tag,tag)
        taglabel[decoded] = value

    #o.add_text("Creation Time","2022:08:18 18:18:18")
    #print(taglabel)
    #print(taglabel['Make'])
    #print(taglabel['Model'])
    #print(taglabel['LensModel'])
    #print(taglabel['Creation Time'])
    return str(taglabel['DateTimeOriginal'])
    # img.save("princess4.png", jpginfo=o)
    # targetImage = img("princess4.png")
    # print(targetImage.text)

t = img_info()
time_stamp = int(time.mktime(time.strptime(t, "%Y:%m:%d %H:%M:%S")))
nowdate = int(time.time())
print(time_stamp)
print(nowdate)
if (time_stamp<nowdate):
    print("FALSE")
 