import sqlite3
import random
import string

# Establish a connection to the SQLite3 database
conn = sqlite3.connect('sayan.db')
cursor = conn.cursor()

# Generate random data for insertion
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_phone():
    return ''.join(random.choice(string.digits) for _ in range(10))

def generate_random_experience():
    return random.randint(1, 30)

def generate_random_education():
    education_options = ['Bachelor', 'Master', 'PhD']
    return random.choice(education_options)

# Insert random data into the user table
for _ in range(100):
    name = generate_random_string(10)
    contact_no = generate_random_phone()
    address = generate_random_string(20)
    father = generate_random_string(10)
    mother = generate_random_string(10)
    job = generate_random_string(15)
    companies = generate_random_string(15)
    experience = generate_random_experience()
    education = generate_random_education()
    institute = generate_random_string(15)

    query = f"INSERT INTO user (name, contactNo, address, father, mother, job, companies, experience, education, institute) " \
            f"VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = (name, contact_no, address, father, mother, job, companies, experience, education, institute)
    cursor.execute(query, values)

# Commit the changes and close the connection
conn.commit()
conn.close()
