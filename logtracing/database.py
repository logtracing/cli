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
                return func(self, connection, *args, **kwargs)
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
            cursor = connection.cursor()
            query = "SELECT COUNT(*) FROM logs"

            cursor.execute(query)
            result = cursor.fetchone()

            return result[0]
        except DBError as e:
            print(e)
