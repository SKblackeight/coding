## pydantic 사용하도록 수정
## 각 함수별 기능 호출을 절차적 실행
import os
import A_detect_car
import A_hash_ck
import A_meta
import A_pop
from pydantic import BaseModel

# File Type
class File(BaseModel):
    path : str
    header : str
    hash : str
    confirmed : bool
    metadata : float
    plate : bool
    delete : bool

if __name__ == "__main__":
    dic_dir ='Detection2/SKB'
    file_list=[]

    # make file_list
    for path, dir, files in os.walk(dic_dir):
        for name in files:
            file_path = os.path.join(path,name)
            file_list.append(File(path=file_path, header="", hash=False, confirmed=False, metadata=0.0, plate=False,delete=False))

    # is jpg?
    for file in file_list:
        with open(file.path, 'rb') as afile:
            magic = afile.read(16)
            header = magic.hex()[0:2]
            if header.upper() == 'FF':
                file.header = "jpg"

    # hash check
    A_hash_ck.hash_com(file_list)
    
    # jpg metadata check
    for file in file_list:
        if file.header == "jpg":
            A_meta.jpg_info(file)

    # car licence check
    for file in file_list:
        if file.header == "jpg" and not(file.confirmed):
            A_detect_car.detect_car(file)
        print(file)

    # popup 
    A_pop.pop(file_list)    #만료일자 지나지 않은 것 팝업


    #             # a = A_hash_ck.hash_com(filedir)
    #             # print(a)
                # if a != None:
                #     A_detect_car.detect_car(a)

    #             b = A_hash_ck.hash_com2(filedir)
                
    #             if b != None:
    #                 # print(b)
    #                 # expiration = float(time.time())
    #                 # A_meta.header_write(filedir, expiration)
                        
    #                 # A_header_ck.header_check(b) #만료일자 지난것은 삭제
                    
    #                 A_header_ck.header_check2(b) #만료일자 지나지 않은 것
    #             file_list.append(filedir)
    # A_pop.pop(file_list)    #만료일자 지나지 않은 것 팝업
