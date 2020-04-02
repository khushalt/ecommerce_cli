import json
from mysql.connector import Error, connect
import logging
import os


class Database:

    def __init__(self):
        db = self.read_db_config()
        self._conn = None
        self.db_name = db.get('db_name')
        self.db_user = db.get('db_user')
        self.db_pwd = db.get('db_pwd')
        self.host = db.get('host')

    def db_connect(self):
        try:
            self._conn = connect(
                host=self.host,
                user=self.db_user,
                passwd=self.db_pwd
            )
            return self._conn
        except Error as e:
            self.db_close()
            raise e

    def db_close(self):
        if self._conn:
            self._conn.close()

    def execute_query(self, curs_obj, query):
        try:
            return curs_obj.execute(query)
        except Exception as e:
            raise e

    @staticmethod
    def read_db_config():
        with open('/home/indictrans/khushal/workspace/ecommerce/ecomm/database/db_config.json', 'r') as db:
            return json.load(db)


db_obj = Database()
db_connection = db_obj.db_connect().cursor(buffered=True)
"""use above connection object throughout application since so many pools slows down"""
