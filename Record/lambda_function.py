import json
import pymysql

class database():
    def __init__(self, dbinfo):
        self.db = pymysql.connect(
            host = dbinfo["host"],
            port = dbinfo["port"],
            user = dbinfo["user"],
            password = dbinfo["passsword"],
            db = dbinfo["db"],
            charset = dbinfo["charset"]
        )
        self.cursor = self.db.cursor()
        self.createTable()

    def createTable(self):
        create_hash_table_query = "CREATE TABLE IF NOT EXISTS hash(value varchar(100) NOT NULL)"
        self.cursor.execute(create_hash_table_query)
        self.db.commit()

    def search(self, data:str) -> str:
        try:
            select_query = "SELECT value FROM hash WHERE value = %s"
            self.cursor.execute(select_query, data)

            if data in self.cursor:
                return data
            else:
                return ""
        except:
            return "Fail"

    def insert(self, data:str) -> bool:
        try:
            insert_query = "INSERT INTO hash (value) VALUES (%s)"
            self.cursor.execute(insert_query, data)
            # self.cursor.executemany(hash, id)
            self.db.commit()
            return True
        except:
            return False

    def close(self):
        self.db.close()

def lambda_handler(event, context):
    # TODO implement
    json_object = {}
    with open("shadow.json") as f:
        json_object = json.load(f)
    db = database(json_object)
    if event == "insert":
        out = db.insert(context)
    else:
        out = db.search(context)
    db.close
    return {
        'statusCode': 200,
        'body': json.dumps(out)
    }