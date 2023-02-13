import sqlite3

with sqlite3.connect("homework20.sqlite") as connection:
    cursor = connection.cursor()
    query = ('CREATE TABLE IF NOT EXISTS users ('
             'id INTEGER PRIMARY KEY AUTOINCREMENT,'
             'first_name TEXT NOT NULL,'
             'last_name TEXT NOT NULL,'
             'age INTEGER)')
    cursor.execute(query)
    connection.commit()