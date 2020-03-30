from ecomm.database.db_connect import db_obj, db_connection
from _collections import  OrderedDict
from ordered_set import OrderedSet


def create_db():
    """check if db exist use db else create new instance"""
    db_obj.execute_query(db_connection, 'Show databases')
    if any(db_obj.db_name in i for i in db_connection):
        db_obj.execute_query(db_connection, 'use ecommerce')
    else:
        db_obj.execute_query(db_connection, 'create database %s' % db_obj.db_name)


def create_tables():
    """Creating Std tables"""
    db_obj.execute_query(db_connection, 'Show Tables')
    tables_to_execute = list(OrderedSet(['User', 'Admin', 'ProductCategory', 'Product', 'Cart']) - set([i[0] for i in db_connection]))
    mapper_ = OrderedDict({
        'User': """Create Table User ( customer_id int NOT NULL, name varchar(255) NOT NULL,
            email varchar(255), address varchar(255), PRIMARY KEY (customer_id))""",
        'Admin': """Create Table Admin ( admin_id int NOT NULL, name varchar(255) NOT NULL,
            email varchar(255), address varchar(255), PRIMARY KEY (admin_id))""",
        'ProductCategory': """Create Table ProductCategory( category_id int NOT NULL, 
            name varchar(255) NOT NULL,description varchar(255),PRIMARY KEY (category_id))""",
        'Product': """Create Table Product ( product_id int NOT NULL, name varchar(255) NOT NULL,
            category_id int not null,description varchar(255),PRIMARY KEY (product_id), 
            foreign key(category_id) references ProductCategory(category_id))""",
        'Cart': """ Create Table Cart ( cart_id int not null, customer_id int,address varchar(255), 
            email varchar(255), product_id int not null, discount_amount int not null, 
            total_amount int not null, PRIMARY KEY (cart_id), foreign key(customer_id) references User(customer_id),
            foreign key(product_id) references Product(product_id))"""

    })
    for query in tables_to_execute:
        db_obj.execute_query(db_connection, mapper_.get(query))


def create_db_schema():
    create_db()
    create_tables()


create_db_schema()
