import glob

path = "./*"
file_list = glob.glob(path)
file_list_jpg = [file for file in file_list if file.endswith(".jpg")]

print("file_list_jpg: {}".format(file_list_jpg))

import glob

path = "./*"
file_list = glob.glob(path)
file_list_png = [file for file in file_list if file.endswith(".png")]

print("file_list_png: {}".format(file_list_png))