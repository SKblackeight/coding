import os
import glob

fromdir = "C:\\Users\\user\\Desktop\\a"
#----- 파일 검색 -----
# for (path, dir, files) in os.walk(fromdir):
#     for filename in files:
#         ext = os.path.splitext(filename)[-1]
#         if ext == '.png' or ext== '.jpg':
#             print("%s/%s" % (path, filename))

#-----파일 삭제 ---------     
# # todir = 'C:\\Users\\user\\Desktop\\b'

os.chdir(fromdir)   
files = glob.glob("*")   
# os.chdir(todir)            
for f in files:               
    os.remove(f)        
    print ("file name[" + f + "]")    
# print(files)
