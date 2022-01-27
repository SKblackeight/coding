import hashlib
from unittest import result
from matplotlib.pyplot import connect
import pymysql

hash = hashlib.sha256()
afile = open('t.png', 'rb')
buf = afile.read()
hash.update(buf)
a= str(hash.hexdigest())
print(a)

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234',db='mydb',charset='utf8')
cursor = conn.cursor()
sql = ('SELECT filehash FROM hashgap ')
cursor.execute(sql)

row= [item[0] for item in cursor.fetchall()]

print(row)
if a in row:
    print(True)
else:
    print(False)
