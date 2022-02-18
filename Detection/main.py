import os
import A_detect_car
import A_header_ck
import A_hash_ck
import A_meta
import A_pop

if __name__ == "__main__":
    dirdir ='Detection/SKB'
   
    file_list=[]    
    for path, dir, files in os.walk(dirdir):
        
        for names in files:
            filedir = os.path.join(path,names)
            
            afile = open(filedir, 'rb')
            magic = afile.read(16)
            a = magic.hex()
            b = a[0:2]

            if b.upper() == 'FF' : 
                
                # a = A_hash_ck.hash_com(filedir)
                # print(a)
                # if a != None:
                #     A_detect_car.detect_car(a)

                b = A_hash_ck.hash_com2(filedir)
                
                if b != None:
                    # print(b)
                    # expiration = float(time.time())
                    # A_meta.header_write(filedir, expiration)
                        
                    # A_header_ck.header_check(b) #만료일자 지난것은 삭제
                    
                    A_header_ck.header_check2(b) #만료일자 지나지 않은 것
                file_list.append(filedir)
    A_pop.pop(file_list)    #만료일자 지나지 않은 것 팝업

        

    