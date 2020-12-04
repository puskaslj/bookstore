import sqlite3

def connect():
    connect_to_db = sqlite3.connect("books.db")
    cursor = connect_to_db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    connect_to_db.commit()
    connect_to_db.close()

def insert(title, author, year, isbn):
    connect_to_db = sqlite3.connect("books.db")
    cursor = connect_to_db.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",(title, author, year, isbn))
    connect_to_db.commit()
    connect_to_db.close()

def view():
    connect_to_db = sqlite3.connect("books.db")
    cursor = connect_to_db.cursor()
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()
    connect_to_db.close()
    return rows

def search(title = "", author = "", year = "", isbn = ""):
    connect_to_db = sqlite3.connect("books.db")
    cursor = connect_to_db.cursor()
    cursor.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    rows = cursor.fetchall()
    connect_to_db.commit()
    connect_to_db.close()
    return rows

def delete(id):
    connect_to_db = sqlite3.connect("books.db")
    cursor = connect_to_db.cursor()
    cursor.execute("DELETE FROM book WHERE id = ?",(id, ))
    connect_to_db.commit()
    connect_to_db.close()

def update(id, title, author, year, isbn):
    connect_to_db = sqlite3.connect("books.db")
    cursor = connect_to_db.cursor()
    cursor.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
    connect_to_db.commit()
    connect_to_db.close()


connect()
#insert("The Govna","Govnovalj", 1999, 2222212)
#delete(2)
#update(1,"Djordje", "Ne znam", 1923, 9001)
#print(view())
#print(search(author="Govnovalj"))