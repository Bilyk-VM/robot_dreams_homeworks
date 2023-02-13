import sqlite3

with sqlite3.connect("homework20.sqlite") as connection:
    cursor = connection.cursor()
    query = ('CREATE TABLE IF NOT EXISTS users ('
             'id INTEGER PRIMARY KEY,'
             'first_name TEXT UNIQUE,'
             'last_name TEXT UNIQUE,'
             'age INTEGER)')
    cursor.execute(query)
    connection.commit()