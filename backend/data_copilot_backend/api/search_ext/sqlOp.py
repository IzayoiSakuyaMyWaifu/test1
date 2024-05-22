"""sql数据库相关操作"""
import pymysql as sql
class sqlOp():
    def __init__(self, db, password="88733167Tj!", host="106.14.142.64", user="root", sql=None):
        self.db = db
        self.host = host
        self.user = user
        self.password = password
        self.SQL = sql

    def getDB_INFO(self):
        conn = sql.connect(host=self.host, user=self.user, password=self.password, database=self.db)
        cur = conn.cursor()

        # 获取所有表名
        cur.execute("SHOW TABLES")
        tables = cur.fetchall()

        db_info = {}

        for table in tables:
            table_name = table[0]

            # 获取每个表的列信息
            cur.execute(f"SHOW COLUMNS FROM {table_name}")
            columns = cur.fetchall()

            # 保存表的列信息
            db_info[table_name] = [
                {'Field': column[0], 'Type': column[1], 'Null': column[2], 'Key': column[3], 'Default': column[4],
                 'Extra': column[5]}
                for column in columns
            ]

        conn.close()
        return db_info

    def excute(self):
        conn = sql.connect(host=self.host, user=self.user, password=self.password, database=self.db)
        cur = conn.cursor()
        cur.execute(self.SQL)
        result = cur.fetchall()
        columns = [desc[0] for desc in cur.description]  # 获取列名
        conn.close()

        # 将结果转换为JSON格式
        json_result = [dict(zip(columns, row)) for row in result]
        return json_result
