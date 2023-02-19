import sqlite3 as db


def init_db():
    with db.connect("main.db") as con:
        cur = con.cursor()
        try:
            cur.execute("""CREATE TABLE blog(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR NOT NULL, 
                content TEXT NOT NULL, 
                date_of_entry datetime NOT NULL
            );""")
            con.commit()
        except db.OperationalError:
            pass
        
        data = ("Some good blog", "This is one of the best blog ever written in the history.", "12/5/2023")

        cur.execute("""
            Insert into blog (title, content, date_of_entry) values(?,?,?)
        """, data)
        con.commit()


def get_db():
    with db.connect("main.db") as con:
        cur = con.cursor()
        cur.execute("""
            Select * from blog;
        """)
        data = cur.fetchall()
        print(data)
get_db()