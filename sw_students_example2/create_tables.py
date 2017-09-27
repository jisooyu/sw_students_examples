import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table= "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)" 
cursor.execute(create_table)

# create_table= "CREATE TABLE IF NOT EXISTS items (name TEXT, price REAL)" 
# cursor.execute(create_table)

# create_table= "CREATE TABLE IF NOT EXISTS stores (name TEXT, price REAL)" 
# cursor.execute(create_table)

connection.commit()
connection.close()