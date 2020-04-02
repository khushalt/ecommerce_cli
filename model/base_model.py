from ecomm.database.db_connect import db_connection, db_obj


class BaseModel:
    database = 'use ecommerce'

    def __init__(self):
        self.parameter = (self.table,) + self.meta + (self.customer_id, self.name, self.email, self.address)

    def on_save(self):
        query_ = """INSERT INTO %s (%s, %s, %s, %s) 
                                VALUES ('%s', '%s', '%s', '%s') """ % self.parameter
        db_obj.execute_query(db_connection, BaseModel.database)
        db_obj.execute_query(db_connection, query_)

    def on_delete(self):
        query_ = """ DELETE from %s"""

    def on_validate(self):
        pass



