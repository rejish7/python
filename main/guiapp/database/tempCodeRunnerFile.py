import sqlite3
conn = sqlite3.connect('college.sqlite3')
cursor =conn.cursor()
def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   firstname TEXT NOT NULL,
                   middlename,
                   lastname TEXT NOT NULL,
                   email TEXT NOT NULL,
                   phone INTEGER ,
                   password TEXT NOT NULL
 
                   )
    """)
    conn.commit()
create_tables()