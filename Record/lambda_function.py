import json
import pymysql

class database():
    def __init__(self):
        self.db = pymysql.connect(
            host="reccar.c4zzcvkkrxzn.ap-northeast-2.rds.amazonaws.com",
            port = 3306,
            user = "recuser",
            password= "6jKDpmrs89adX2Op5KiP",
            db = "recdb",
            charset="utf8"
        )
        self.cursor = self.db.cursor()
        self.createTable()

    def createTable(self):
        create_hash_table_query = "CREATE TABLE IF NOT EXISTS hash(value varchar(100) NOT NULL)"
        self.cursor.execute(create_hash_table_query)
        self.db.commit()

    def search(self, data:str) -> bool:
        try:
            select_query = "SELECT value FROM hash WHERE value = %s"
            self.cursor.execute(select_query, data)

            if data in self.cursor:
                return True
            else:
                return False
        except:
            return None

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
    db = database()
    if event == "insert":
        out = db.insert(context)
    else:
        out = db.search(context)
    db.close
    return {
        'statusCode': 200,
        'body': json.dumps(out)
    }