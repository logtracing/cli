from typing import List
from mysql.connector import connect, Error as DBError
from mysql.connector.connection import MySQLConnection

from logtracing import config
from logtracing.entities.logs import Log, LogLevel

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
    def __init__(self) -> None:
        database_config = config.get_database_config()

        self.user = database_config['user']
        self.password = database_config['pass']
        self.host = database_config['host']
        self.port = database_config['port']
        self.database = database_config['db_name']

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
    def get_logs(self, flow: str, limit: int, filter: str, transport: LogLevel, connection: MySQLConnection) -> List[Log]:
        try:
            with connection.cursor() as cursor:
                where_query = f"WHERE l.flow = '{flow}'"

                if filter:
                    where_query = f"{where_query} AND l.content LIKE '%{filter}%'"

                if transport:
                    where_query = f"{where_query} AND l.level = '{transport.value}'"

                query = f'''
                    SELECT l.level, l.flow, l.content, l.createdAt as created_at, lg.name as group_name
                    FROM logs l
                    LEFT JOIN logGroups lg ON lg.id = l.logGroupId
                    {where_query}
                    ORDER BY l.createdAt DESC
                    LIMIT {limit}
                '''

                cursor.execute(query)
                result = cursor.fetchall()

                logs = [Log(*log) for log in result]

                return logs
        except DBError as e:
            print(e)
