from ecomm.database.db_connect import db_obj, db_connection


def create_db():
    """check if db exist use db else create new instance"""
    db_obj.execute_query(db_connection, 'Show databases')
    if any(db_obj.db_name in i for i in db_connection):
        db_obj.execute_query(db_connection, 'use ecommerce')
    else:
        db_obj.execute_query(db_connection, 'create database %s' % db_obj.db_name)


def create_tables():
    """Creating two std table of User and Adimin"""
    db_obj.execute_query(db_connection, 'Show Tables')
    query_ = ["""CREATE TABLE User ( customer_id int NOT NULL, name varchar(255) NOT NULL,
            ,email varchar(255), address varchar(255), PRIMARY KEY (customer_id))""",
              """CREATE TABLE Admin ( admin_id int NOT NULL, name varchar(255) NOT NULL,
        ,email varchar(255), address varchar(255), PRIMARY KEY (admin_id)"""]
    for query in query_:
        db_obj.execute_query(db_connection, query)


def create_db_schema():
    create_db()
    create_tables()


create_db_schema()
