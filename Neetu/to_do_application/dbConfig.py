import os
import json

# print(os.path.dirname(__file__), __file__)
__DATABASE_FILE = os.path.join(os.path.dirname(__file__), "database.json")  # Absolute path to the database file
# print(__DATABASE_FILE)

# read the database from json file
if not os.path.exists(__DATABASE_FILE):
    try:
        with open(__DATABASE_FILE, 'w') as f:  # write the database file
            json.dump({}, fp=f, indent=4)  # writes the empty database file
    except Exception:
        os.remove(__DATABASE_FILE)

DATABASE = json.load(open(__DATABASE_FILE, 'r'))

# for item in DATABASE.items()[::-1][:5]:
#     print(item)


def write_db(database):
    with open(__DATABASE_FILE, 'w') as db_file:
        json.dump(DATABASE, db_file, indent=4)
