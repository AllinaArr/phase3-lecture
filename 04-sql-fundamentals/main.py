import sqlite3

connection = sqlite3.connect("chinook.db") #connect to database

cursor = connection.cursor() #get the cursor

result = cursor.execute('SELECT * FROM artists') #execute query

for row in result:
    print(row)
    
sql = """
INSERT INTO ARTISTS (Name)
VALUES
("Tennis")
"""
cursor.execute(sql)
connection.commit() #commit the transactions (save to db)