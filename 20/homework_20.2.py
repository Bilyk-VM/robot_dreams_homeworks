import sqlite3
from pprint import pprint

with sqlite3.connect("homework20.sqlite") as connection:
    cursor = connection.cursor()

    person = [
        ('Guido', 'Van Rossum', 67),
        ('Linus', 'Torvalds', 54),
        ('Mark', 'Zuckerberg', 39),
        ('Elon', 'Musk', 52),
        ('Bill', 'Gates', 68), ]

    query = 'INSERT INTO users (first_name, last_name, age) values (?, ? , ?)'
    cursor.executemany(query, person)
    connection.commit()

    query = 'SELECT * FROM users'
    res = cursor.execute(query)
    pprint(res.fetchall())