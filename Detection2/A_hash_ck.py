import hashlib                       
import pymysql
import requests
import json

def hash_com (file_list):
    # query
    query_list = []
    for file in file_list:
        if file.header != "jpg":
            pass
        hash = hashlib.sha256()
        afile = open(file.path, 'rb')
        buf = afile.read()
        hash.update(buf)
        file.hash = str(hash.hexdigest())
        query_list.append(str(hash.hexdigest()))
    response_list = query_hash(query_list)
    
    # check
    for file in file_list:
        if file.hash in response_list:
            file.confirmed = True
    

def hash_com2 (filedir):
    hash = hashlib.sha256()
    afile = open(filedir, 'rb')
    buf = afile.read()
    hash.update(buf)
    a= str(hash.hexdigest())
    # print(a)

    conn = pymysql.connect(host='127.0.0.1', user='root', password='',db='',charset='utf8') #RDS STORAGE #pw 입력 / DB 입력
    cursor = conn.cursor()
    sql = ('SELECT filehash FROM hashgap ')
    cursor.execute(sql)

    row= [item[0] for item in cursor.fetchall()]

    # print(row)
    afile.close()
    if a in row:
        return filedir
    else:
        return None

def query_hash (query_list):
    hash_list = json.dumps({"hash_list":query_list})
    url = "https://tptbrdc0i5.execute-api.ap-northeast-2.amazonaws.com/RecodeAPI"
    response = requests.post(url, data=hash_list, timeout=6) #3초 지나면 exception 발생
    return response.text