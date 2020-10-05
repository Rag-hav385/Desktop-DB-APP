import sqlite3
'''
connect to database
create a cursor object
write an sql query
commit changes

'''
def connect():
    conn = sqlite3.connect("books.db")
    cur  = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY , tittle text , author text , year integer , isbn integer) ")
    conn.commit()
    conn.close()

def insert(tittle,year,author,isbn):
    conn = sqlite3.connect("books.db")
    cur  = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(tittle,author,year,isbn))
    conn.commit()
    conn.close()

def view():
     conn = sqlite3.connect("books.db")
     cur  = conn.cursor()
     cur.execute("SELECT * FROM book")
     rows = cur.fetchall()
     conn.close()
     return rows

def search(tittle = "",author = "",year = "",isbn = ""):
    conn = sqlite3.connect("books.db")
    cur  = conn.cursor()
    cur.execute("SELECT * FROM book WHERE tittle = ? OR author = ? OR year = ? OR isbn = ?",(tittle,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur  = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(id,tittle,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur  = conn.cursor()
    cur.execute("UPDATE book SET tittle = ? , author = ? , year = ? , isbn = ? WHERE id = ?",(tittle,author,year,isbn,id))
    conn.commit()
    conn.close()


connect()
update(1,"English","Raghav",1994,122)
insert("Maths",1944,"RDSHARMA",111222333)
insert("Biology",1984,"RohanJoshi",222333444)

print(view())
