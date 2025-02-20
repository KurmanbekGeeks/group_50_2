# main_db.py
import sqlite3
from db import queries

db = sqlite3.connect('db/db.sqlite')
cursor = db.cursor()

async def create_tables():
    if db:
        print('База данных подключена')
    cursor.execute(queries.TABLE_registered)
    cursor.execute(queries.CREATETABLE_store)
    cursor.execute(queries.CREATETABLE_store_detail)


async def sql_insert_registered(fullname, age, gender, date_age, email, photo):
    cursor.execute(queries.INSERT_TABLE_registered, (fullname, age, gender, date_age, email, photo))
    db.commit()


async def sql_insert_store(name_product, size, price, photo, product_id):
    cursor.execute(queries.INSERT_store,
                   (name_product, size, price, photo, product_id)
                   )

    db.commit()


async def sql_insert_store_detail(product_id, info_product, category):
    cursor.execute(queries.INSERT_store_detail,
                   (product_id, info_product, category))
    db.commit()