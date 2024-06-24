import sqlite3
conn = sqlite3.connect('college.sqlite3')
cursor =conn.cursor()
def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   firstname TEXT NOT NULL,
                   lastname TEXT NOT NULL,
                   email TEXT NOT NULL,
                   phone INTEGER ,
                   password TEXT NOT NULL
 
                   )
    """)
    conn.commit()
create_tables()

def insert(firstname,lastname,email,phone,password):
    cursor.execute("""
    INSERT INTO students(firstname,lastname,email,phone,password) VALUES(?,?,?,?,?)
    """, (firstname,lastname,email,phone,password))
    conn.commit()

def show():
    cursor.execute("""
    SELECT * FROM students
    """)
    data = cursor.fetchall()
    # data = cursor.fetchone()
    # data = cursor.fetchmany(2)
    print(data)
show() 
def delete(id):
    cursor.execute("""
    DELETE FROM students WHERE id = ?
    """,(id,))
    conn.commit()
# delete(1)



def update(firstname,lastname,email,phone,password):
    cursor.execute("""
    UPDATE students SET firstname = ?, password = ? WHERE id = ?
    """,(firstname,lastname,email,phone,password))
    conn.commit()
# update()

firstname = input("Enter your firstname")
lastname = input("Enter your lastname")
email = input("Enter your email")
phone = input("Enter your phonenumber")
password = input("Enter your password")

insert(firstname,lastname,email,phone,password)





