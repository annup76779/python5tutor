import sqlite3 

def get_con():
    con = sqlite3.connect("main.sqlite3")
    return con

def create_table(con):
    cursor = con.cursor()
    try:
        cursor.execute('''
            create table test(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255) NOT NULL,
                age INTEGER NOT NULL
            )
        ''')
    except Exception as e:
        print(e)
    finally:
        cursor.close()


def insert_data(con, data):
    cursor = con.cursor()
    try:
        cursor.executemany('''
            INSERT INTO test (name, age) VALUES (?, ?)
        ''', data)

        # commit the data to database
        con.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()


def main():
    con = get_con()
    cursor = con.cursor()

    try:
        # insert_data(con, (("Anurag Pandey", 22), ("Ayushi Yadav", 23), ("Shashank Pandey", 22), ("Abhinav Lala", 24)))
        cursor.execute("""SELECT * FROM test WHERE name like "A%";""")

        output = cursor.fetchall()
        print(output)
    except Exception as e:
        print(e)
    finally:
        cursor.close()

main()