import os 
import getpass


booksData=[
    {'name':'The Alchemist','author':'Paulo Coelho','price':500,'quantity':10,'category':'Adventure'},
     {'name':'The Da Vinci Code','author':'Dan Brown','price':800,'quantity':5,'category':'Mystery'},
    {'name':'Think and Grow Rich','author':'Napoleon Hill','price':700,'quantity':3,'category':'Business'},

]
if not os.path.exists("books/database.txt"):
    open("books/database.txt", "w").close()

def register():
    username = input("Enter username: ").strip()
    if username in open("books/database.txt", "r").read():
        print("Username already exists")
        exit()
    password = getpass.getpass("Enter password: ").strip()
    c_password = getpass.getpass("Confirm password: ").strip()
    if password != c_password:
        print("Passwords do not match")
        exit()

    data =f"username:{username},password:{password}\n"
    with open("books/database.txt", "a") as f:
        f.write(data)
    print("User registered successfully")
        
    




def login():
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ").strip()
    data = open("books/database.txt", "r").readlines()
    is_login=False
    for user in data:
        user = user.split(",")
        uname = user[0].split(":")[1]
        upass = user[1].split(":")[1]
        upass = upass[:-1]
        if username == uname and password == upass:
            is_login=True
           
            
    if is_login:
        print("Welcome",username)
        for book in booksData:
            print(f"Name: {book['name']}, Author: {book['author']}, Price: {book['price']}, Quantity: {book['quantity']}, Category: {book['category']}")
    else:
        print("Invalid credentials")
        exit()
       






question = input("Do you have an account? (y/n): ").strip()
if question == "n":
    register()
else:
    login()