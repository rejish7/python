import tkinter as tk
from tkinter import Tk
import sqlite3
conn = sqlite3.connect('college.sqlite3')
cursor =conn.cursor()
def submit_form():
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
submit_form()

def insert(firstname,lastname,email,phone,password):
    cursor.execute("""
    INSERT INTO STUDENTS(firstname,lastname,email,phone,password) VALUES(?,?,?,?,?)
    """, (firstname,lastname,email,phone,password))
    conn.commit()

root = tk.Tk()  


firstname = tk.StringVar()
tk.Label(root, text="First Name").grid(row=0)
tk.Entry(root, textvariable=firstname).grid(row=0, column=1)

middlename = tk.StringVar()
tk.Label(root, text="Middle Name").grid(row=1)
tk.Entry(root, textvariable=middlename).grid(row=1, column=1)

lastname = tk.StringVar()
tk.Label(root, text="Last Name").grid(row=2)
tk.Entry(root, textvariable=lastname).grid(row=2, column=1)

email = tk.StringVar()
tk.Label(root, text="Email").grid(row=3)
tk.Entry(root, textvariable=email).grid(row=3, column=1)

phone = tk.StringVar()
tk.Label(root, text="Phone").grid(row=4)
tk.Entry(root, textvariable=phone).grid(row=4, column=1)

password = tk.StringVar()
tk.Label(root, text="Password").grid(row=5)
tk.Entry(root, textvariable=password, show='*').grid(row=5, column=1)

tk.Button(root, text="Submit", command=submit_form).grid(row=6, column=1)

insert(firstname,lastname,email,phone,password)
root.mainloop()
