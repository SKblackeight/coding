import hashlib                       
import pymysql

def hash_com (filedir):
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

    if a not in row:
        return filedir
    else:
        return None

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