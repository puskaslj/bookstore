import sqlite3

class Database:

    def __init__(self):
        self.connect_to_db = sqlite3.connect("books.db")
        self.cursor = self.connect_to_db.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.connect_to_db.commit()

    def insert(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",(title, author, year, isbn))
        self.connect_to_db.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM book")
        rows = self.cursor.fetchall()
        return rows

    def search(self, title = "", author = "", year = "", isbn = ""):
        self.cursor.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
        rows = self.cursor.fetchall()
        self.connect_to_db.commit()
        return rows

    def delete(self, id):
        self.cursor.execute("DELETE FROM book WHERE id = ?",(id, ))
        self.connect_to_db.commit()

    def update(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        self.connect_to_db.commit()

    def __del__(self):
        self.connect_to_db.close()

#insert("The Govna","Govnovalj", 1999, 2222212)
#delete(2)
#update(1,"Djordje", "Ne znam", 1923, 9001)
#print(view())
#print(search(author="Govnovalj"))