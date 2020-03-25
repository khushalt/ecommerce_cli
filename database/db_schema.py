from ecomm.database.db_connect import db_obj, db_connection


def validate_db_exist():
    db = db_obj.execute_query(db_connection, 'Show databases')


def create_db_schema():
    # validate_db_exist()
    query_ = 'create database %s' % db_obj.db_name
    data = db_obj.execute_query(db_connection, query_)
    print(data)
