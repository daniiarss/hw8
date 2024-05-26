# SQL - язык структурированных запросов
# база данных -
# СУБД - система управления базами данных
# NOsql:SQL
# posgreSQL, mySQL, SQLite3-2

import sqlite3

db = sqlite3.connect('op_36_3test.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS user (
    lastname TEXT,
    age INTEGER,
    view INTEGER,
    bitday DATE
)''')
cursor.execute('''INSERT INTO user VALUES ("beka",49,5,'2003-87-99')''')
cursor.execute('''INSERT INTO user VALUES ("sam",46,4,'2003-88-11')''')
cursor.execute('''UPDATE user SET age=99 WHERE rowid != 2 ''')
cursor.execute('''SELECT rowid, * FROM user''')
a = cursor.fetchall()
print("Данные до удаления:")
for i in a:
    print(i)
db.commit()

def delete_even_rowids():
    conn = sqlite3.connect('op_36_3test.db')
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM user
    WHERE rowid % 2 = 0
    ''')
    conn.commit()
    conn.close()
delete_even_rowids()
db = sqlite3.connect('op_36_3test.db')
cursor = db.cursor()
cursor.execute('''SELECT rowid, * FROM user''')
a = cursor.fetchall()
print("\nДанные после удаления записей с четным rowid: ")
for i in a:
    print(i)
db.commit()
db.close()
