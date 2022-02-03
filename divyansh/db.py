import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def create(self, *query_params):
        try:
            for query in query_params:
                self.cur.execute(query)
            return True
        except Exception as e:
            print(e)
            return False

    def insert(self,query, params):
        try:
            if len(params) < 4:
                raise Exception("Minumum amount of parameters is 4")
            self.cur.executemany(query, params)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def show_table(self):
        tables = self.cur.execute("""SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';""")
        return tables.fetchall()

    def connection(self):
        return self.conn
    def cursor(self):
        return self.cur

if __name__ == '__main__':
    db = Database("database.db")
    # db.create(
    #     "CREATE TABLE IF NOT EXISTS Studend(Stud_name TEXT NOT NULL, Stud_id INTEGER Not NULL, Dept_id INTEGER NOT NULL)",
    #     """CREATE TABLE IF NOT EXISTS Department(Dept_id INTEGER PRIMARY KEY NOT NULL, Dept_name TEXT NOT NULL, Dept_loc TEXT NOT NULL)"""
    # )
    # db.insert(
    #     "INSERT INTO Studend(Stud_name, Stud_id,Dept_id) VALUES (?,?,?)",
    #     [("Anurag", "1", "356"), ("Divyansh", "2", "356"), ("Shashank", "3", "356"),("Abhinav", "4", "357"), ("Ayushi", "5", "357"), ("Avantika", "6", "358"), ("Sheyash", "7", "359"),("Priya", "8", "360")]
    # )
    # db.insert(
    #     "INSERT INTO Department(Dept_id, Dept_name, Dept_loc) VALUES (?,?,?)",
    #     [(356,"IT", "76"),(357,"CS","78"),(358,"ECE","77"),(359,"IC","80")]
    # )
    conn = db.connection()
    cur = db.cursor()
    # qeury = """
    #     UPDATE Studend
    #     SET Stud_name = ?
    #     WHERE Stud_id = ?
    # """
    # cur.execute(qeury, ("Divyansh Singh", 2))
    # conn.commit()

    query = """
        SELECT * FROM Studend INNER JOIN Department using(Dept_id)
    """
    data = cur.execute(query).fetchall()
    for i in data:
        print(i)
    for i in db.show_table():
        print(i[0])
