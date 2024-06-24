import sqlite3
conn = sqlite3.connect('employee.sqlite3')
cursor =conn.cursor()
def tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   email TEXT NOT NULL,
                   salary  NOT NULL ,
                   department TEXT NOT NULL
 
                   )
    """)
    conn.commit()
tables() 

def insert(name,email,salary,department):
    cursor.execute("""
    INSERT INTO employee(name,email,salary,department) VALUES(?,?,?,?)
    """, (name,email,salary,department))
    conn.commit()

def show():
    cursor.execute("""
    SELECT * FROM employee
    """)
    data = cursor.fetchall()
    # data = cursor.fetchone()
    # data = cursor.fetchmany(2)
    print(data)
show() 
def delete(id):
    cursor.execute("""
    DELETE FROM employee WHERE id = ?
    """,(id,))
    conn.commit()
# delete(1)



def update(name,email,salary,department):
    cursor.execute("""
    UPDATE employee SET name = ?, address = ? WHERE id = ?
    """,(name,email,salary,department))
    conn.commit()
# update(2,"ram","ktm")

name = input("Enter your name")
email = input("Enter your email")
salary = input("Enter your salary")
department = input("Enter your department")
insert(name,email,salary,department)




