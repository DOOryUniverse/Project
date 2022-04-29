import pymysql

class Database():
    def __init__(self):
        self._db = pymysql.connect(
        user = "dbmasteruser",
        passwd = "r,3Ipn|O7mL2vL4S)9Q~;7QVdHMV6R9j",
        host ="ls-a20f4420f7aa9967e25c1e0aecf4d8b641af5f13.cgtgapkuvqbt.ap-northeast-2.rds.amazonaws.com",
        db = "stock",
        port=3306
        )
        self.cursor = self._db.cursor(pymysql.cursors.DictCursor)

    def execute(self, input_sql, input_value = {}):
        self.cursor.execute(input_sql, input_value)

    def executeAll(self, input_sql, input_value = {}):
        self.cursor.execute(input_sql, input_value)
        self.result = self.cursor.fetchall()
        return self.result 

    def commit(self):
        self._db.commit()
        
        
