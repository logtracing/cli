from mysql.connector import connect, Error as DBError
from mysql.connector.connection import MySQLConnection

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
    def get_logs(self, flow: str, connection: MySQLConnection) -> any:
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

                for row in result:
                    print(row)
        except DBError as e:
            print(e)
