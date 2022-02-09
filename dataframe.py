import pandas

import os

dir = 'C:\Work\VS\dataset'

files = os.listdir(dir)

global dataframeFile #데이터프레임의 전역화

#데이터프레임초기화

dataframeFile  = pandas.DataFrame(index=range(0,0), columns=['이름']) 

def file_search(dir, dataframeFile) :

    files = os.listdir(dir)

    for file in files : 

        fullname_file = os.path.join(dir, file)

        if os.path.isdir(fullname_file) : 

            dataframeFile = file_search(fullname_file, dataframeFile)  #재귀함수 호출

        else :

            name, ext = os.path.splitext(file)            

            dic_file = {'이름':name}

            dataframeFile = dataframeFile.append(dic_file, ignore_index = True)

 

    #데이터프레임 리턴

    return dataframeFile

#재귀함수 호출

dataframeFile = file_search(dir,dataframeFile)

#데이터프레임 결과출력
print(dataframeFile)

