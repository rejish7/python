import tkinter as tk 
# messagebox is used to show some message to the user 
from tkinter import messagebox 
 
# ===============Database Connection================ 
import sqlite3 
conn = sqlite3.connect('school.sqlite3') 
cursor = conn.cursor() 
 
# ===============Create Table================ 
cursor.execute('''CREATE TABLE IF NOT EXISTS students 
             ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            email TEXT, 
            gender TEXT, 
            Age INTEGER   
               ) 
              ''') 
 
root = tk.Tk() 
root.title("Students record") 
root.geometry("500x500") 
 
name_label = tk.Label(root, text="Name") 
name_label.pack() 
name_input = tk.Entry(root) 
name_input.pack() 
 
 
 
gender_label = tk.Label(root, text="Gender") 
gender_label.pack() 
gender_input = tk.Entry(root) 
gender_input.pack() 
 
email_label = tk.Label(root, text="Email") 
email_label.pack() 
email_input = tk.Entry(root) 
email_input.pack() 
 
 
age_label = tk.Label(root, text="Age") 
age_label.pack() 
age_input = tk.Entry(root) 
age_input.pack() 
 
def insert_data(): 
    name = name_input.get() 
    email = email_input.get() 
    gender = gender_input.get() 
    age = age_input.get() 
    cursor.execute("""INSERT INTO students  
                   (name, email,gender,age) VALUES (?, ?,?,?)""", (name, email,gender,age)) 
    conn.commit() 
    print("Record inserted successfully") 
    messagebox.showinfo("Success", "Record inserted successfully") 
 
button = tk.Button(root, text="Add Record", command=insert_data) 
button.pack() 
 
root.mainloop()