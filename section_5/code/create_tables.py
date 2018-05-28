import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text,password text)"
# Execute table creation
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
# Execute table creation
cursor.execute(create_table)

cursor.execute("INSERT INTO items VALUES ('test', 12.99)")

# Commit changes to database
connection.commit()

# Close connection
connection.close()
