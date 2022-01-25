# from paramiko import HostKeys
# import pymysql
# import sys

# try:
#     conn = mariadb.connect(
#         user = "root",
#         password = "1234",
#         host = "localhost",
#         port = 3306,
#         database="mydb"
#     )
# except mariadb.Error as e:
#     print(f"Error connecting to MariaDB Platform: {e}")
#     sys.exit(1)

# cur = conn.cursor()

# select_all_query = "SELECT * from mydb"
# cur.execute(select_all_query)

# resultset = cur.fetchall

# print('-------- select all data ----------')
# for firstname, lastname in resultset: 
#     print(f"First name: {firstname}, Last name: {lastname}")

from unittest import result
import pymysql

def dbconnect() :
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234',db='mydb',charset='utf8')
    return conn

def search_data(conn):
    cur = conn.cursor()
    sql = 'SELECT * FROM hashgap'
    cur.execute(sql)
    results = cur.fetchall()
    print(results)

#def compare_data():    
    

def main():
    conn = dbconnect()
    print('연결완료')
    search_data(conn)
    conn.close()
    print('연결해제')

if __name__=="__main__" :
    main()