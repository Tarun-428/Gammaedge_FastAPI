import uuid
import datetime
from contextlib import contextmanager
import time
import psycopg2
from sqlalchemy import null


class ConnectionFailedError(Exception):
    pass
class QueryTimeOutError(Exception):
    pass
class MaxRetriesExceededError(Exception):
    pass

url = "postgresql://postgres:ugWrWQWzzFoTeCGdbzNKQaLTWPEGRswz@yamabiko.proxy.rlwy.net:22331/railway"
urls = "postgresql://postgres:tarun@localhost:5432/gamma_db"
# dbname="gamma_db",
#                 user="postgres",
#                 password="tarun",
#                 host="localhost",
#                 port="5432"
class DatabaseConn:
    def __init__(self):
        self.connection_id = uuid.uuid4()
        self.status = "active"
        self.created_at = datetime.datetime.now()
        print("Con is created!")

    def connect(self):
        # try:
        #     self.conn = psycopg2.connect(url)
        #     print("Connection Successfull!",self.connection_id)
        #     return self.conn
        # except ConnectionFailedError:
        #     print("Connection Failed!",ConnectionFailedError)
        # except Exception as e:
        #     print(e)
        try:
            print(f"conn is connectingg...")
            time.sleep(0.1)
            print("Connection Successfully!")
        except ConnectionFailedError:
            print("unable to connect",ConnectionFailedError)
        except Exception as e:
            print(e)

    def disconnect(self):
        print("Disconnecting connection..",self.connection_id)
        # self.conn.close()
        self.status = "idle"
        print("Successfully close")
    def executeQuery(self,query):
        if self.status != "active":
            raise ConnectionFailedError
        try:
            # self.cursor = self.conn.cursor()
            # self.cursor.execute(query)
            # if query.strip().upper().startswith("SELECT"):
            #     results = self.cursor.fetchall()
            #     for row in results:
            #         print(row)
            #     return results
            # self.conn.commit()
            print("Executed!",self.connection_id)
        except QueryTimeOutError:
            print("Unable to execute query",QueryTimeOutError)

    def is_alive(self):
        if self.status=="active":
            print("Connection is active!")
        else:
            print("connection closed")

class ConnectionPool():
    max_connection = 4
    def __init__(self):
        self._active =  []
        self._idle = []
    def get_connection(self):
        total_con = len(self._active + self._idle)
        print(total_con)
        if self._idle:
            conn = self._idle.pop()
        elif  total_con < self.max_connection:
            conn = DatabaseConn()
            conn.connect()
        else:
            raise ConnectionFailedError("Already Pool is full!")
        conn.status = "active"
        self._active.append(conn)
        return conn
    def release_connection(self,conn:DatabaseConn):
        if conn not in self._active:
            print("Already released")
            return
        self._active.remove(conn)
        conn.status = "idle"
        self._idle.append(conn)
        print("Connection released!")

    def close_all(self):
        for conn in self._active+self._idle:
            conn.disconnect()
        self._active.clear()
        self._idle.clear()
    def get_stats(self):
        print('active',self._active)
        print('idle',self._idle)


    @contextmanager
    def connection(self):
        conn = self.get_connection()
        try:
            yield conn
        finally :
            print("finally",conn.connection_id)
            self.release_connection(conn)

#
# db1 = DatabaseConn()
# db2 = DatabaseConn()
#
# db1.connect(urls)
# db2.connect(url)
#
# db1.executeQuery("select * from users")
# db2.executeQuery("select * from employees")
#
# db1.disconnect()
# db2.disconnect()

pool = ConnectionPool()
with (pool.connection() as conn1, pool.connection() as conn3, pool.connection() as conn4):
    conn1.executeQuery("select * from students")
    conn3.executeQuery("select * from students")
    conn4.executeQuery("select * from students")
pool.get_stats()
with pool.connection() as conn2:
    conn2.executeQuery("select * from teachers")
# pool.get_connection()
    # conn2.is_alive()
pool.get_stats()
# pool.close_all()

