from typing import List
from mysql.connector import connect, Error as DBError
from mysql.connector.connection import MySQLConnection

from entities.logs import Log

def db_connect(func):
    def wrapper(self, *args, **kwargs):
        try:
            with connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            ) as connection:
                return func(self, connection=connection, *args, **kwargs)
        except DBError as e:
            print(e)

    return wrapper

class LogTracingDB:
    def __init__(self, user: str, password: str, host: str, port: int, database: str) -> None:
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    @db_connect
    def total_of_logs(self, connection: MySQLConnection) -> int:
        try:
            with connection.cursor() as cursor:
                query = "SELECT COUNT(*) FROM logs"

                cursor.execute(query)
                result = cursor.fetchone()

                return result[0]
        except DBError as e:
            print(e)

    @db_connect
    def get_logs(self, flow: str, connection: MySQLConnection) -> List[Log]:
        try:
            with connection.cursor() as cursor:
                query = f'''
                    SELECT l.level, l.flow, l.content, l.createdAt as created_at, lg.name as group_name
                    FROM dev_logtracing.logs l
                    LEFT JOIN dev_logtracing.logGroups lg ON lg.id = l.logGroupId
                    WHERE l.flow = '{flow}'
                '''

                cursor.execute(query)
                result = cursor.fetchall()

                logs = [Log(*log) for log in result]
                print(logs[0].text())
                return logs
        except DBError as e:
            print(e)

if __name__ == '__main__':
    db = LogTracingDB(
        user='root',
        password='p4ssw0rd',
        host='127.0.0.1',
        port=3308,
        database='dev_logtracing'
    )

    print(db.get_logs(flow='More Logs Usage'))
