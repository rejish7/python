import tkinter as tk
from tkinter import Tk
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect('login.sqlite3')
cursor =conn.cursor()
def submit_form():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS login(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   firstname TEXT NOT NULL,
                   lastname TEXT NOT NULL,
                   email TEXT NOT NULL,
                   phone integer ,
                   gender TEXT NOT NULL
 
                   )
    """)
    conn.commit()
    insert(firstname.get(),lastname.get(),email.get(),phone.get(),gender.get())
    firstname.set('')
    lastname.set('')
    email.set('')
    phone.set('')
    gender.set('')

def insert(firstname,lastname,email,phone,gender):
    cursor.execute("""
    INSERT INTO login(firstname,lastname,email,phone,password) VALUES(?,?,?,?,?)
    """, (firstname,lastname,email,phone,gender))
    conn.commit()
    print("Record inserted successfully")
    messagebox.showinfo("Success", "Record inserted successfully")


def update(name,email,salary,department):
    cursor.execute("""
    UPDATE login SET name = ?, gender = ? WHERE id = ?
    """,(firstname,lastname,email,phone,gender))
    conn.commit()
# update(2,"ram","ktm")
root = tk.Tk()  
root.title("login page")
root.geometry("500x500")
root.config(bg='#003366')

firstname = tk.StringVar()
tk.Label(root, text="First Name").grid(row=0)

tk.Entry(root, textvariable=firstname).grid(row=0, column=1)

lastname = tk.StringVar()
tk.Label(root, text="Last Name").grid(row=2)
tk.Entry(root, textvariable=lastname).grid(row=2, column=1)

email = tk.StringVar()
tk.Label(root, text="Email").grid(row=3)
tk.Entry(root, textvariable=email).grid(row=3, column=1)

phone = tk.StringVar()
tk.Label(root, text="Phone").grid(row=4)
tk.Entry(root, textvariable=phone).grid(row=4, column=1)

gender = tk.StringVar()
tk.Label(root, text="gender").grid(row=5)
tk.Entry(root, textvariable=gender).grid(row=5, column=1)

tk.Button(root, text="Submit", command=submit_form).grid(row=6, column=1)



root.mainloop()
