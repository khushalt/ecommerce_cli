from ecomm.database.db_connect import Database, Error
import  traceback


class BaseModel:
    database = 'use ecommerce'

    def __init__(self):
        self.parameter = (self.table,) + self.meta + (self.customer_id, self.name, self.email, self.address)
        self.db_attr = Database()
        self.connect = self.db_attr.db_connect()
        self.cursor_ = self.connect.cursor()
        self.db_attr.execute_query(self.cursor_, BaseModel.database)

    def on_save(self):
        try:
            query_ = """INSERT INTO %s (%s, %s, %s, %s) 
                                    VALUES ('%s', '%s', '%s', '%s') """ % self.parameter

            self.db_attr.execute_query( self.cursor_, query_)
            self.connect.commit()
        except Error as e:
            self.exception_activity(e)

    def on_delete(self):
        try:
            query_ = """ DELETE from %s""" %self.parameter[0]
            self.db_attr.execute_query(self.cursor_, query_)
        except Error as e:
            self.exception_activity(e)

    def exception_activity(self, e):
        self.connect.rollback()
        self.db_attr.db_close()
        print("There was an issue while executing", e, traceback.print_exc())
        raise e
