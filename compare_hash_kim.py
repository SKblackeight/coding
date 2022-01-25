import hashlib
from unittest import result
from matplotlib.pyplot import connect
import pymysql

hash = hashlib.md5()
afile = open('t.png', 'rb')
buf = afile.read()
a= str(hash.hexdigest())
print(a)



conn = pymysql.connect(host='127.0.0.1', user='root', password='1234',db='mydb',charset='utf8')
cursor = conn.cursor()
sql = ('SELECT filehash FROM hashgap')
cursor.execute(sql)

for b in cursor:
    print(b)

print ( a == b)