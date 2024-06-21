import tkinter as tk

app= tk.Tk()
app.title("My Calculator")
app.geometry("450x450")
app.config(bg='#003366')

result=tk.Entry(width=40,font="60")
result.grid(padx=20,pady=35,row=0,column=0,columnspan=5)

def take_input(params):
    cvalue = result.get()
    result.delete(0,tk.END)
    result.insert(0,str(cvalue)+str(params))
    

def equal_value():
    current = result.get()
    total = eval(current)
    result.delete(0, tk.END)
    result.insert(0, total)

def clear_value():
     result.delete(0, tk.END)

    
def back_space():
 inputvalue = result.get()
 result.delete(0, tk.END)
 result.insert(0, inputvalue[:-1] )

def percentage():
 current = result.get()
 total = eval(current) / 100
 result.delete(0, tk.END)
 result.insert(0, total)

# def Square():
#  current = result.get()
#  total = eval(current) **2
#  result.delete(0, tk.END)
#  result.insert(0, total)

zero = tk.Button(app, text="0", padx=40, pady=20,command=lambda:take_input("0"))
one = tk.Button(app, text="1", padx=40, pady=20,command=lambda:take_input("1"))
two = tk.Button(app, text="2", padx=40, pady=20,command=lambda:take_input("2"))
three = tk.Button(app, text="3", padx=40, pady=20,command=lambda:take_input("3"))
four = tk.Button(app, text="4", padx=40, pady=20,command=lambda:take_input("4"))
five = tk.Button(app, text="5", padx=40, pady=20,command=lambda:take_input("5"))
six = tk.Button(app, text="6", padx=40, pady=20,command=lambda:take_input("6"))
seven = tk.Button(app, text="7", padx=40, pady=20,command=lambda:take_input("7"))
eight = tk.Button(app, text="8", padx=40, pady=20,command=lambda:take_input("8"))
nine = tk.Button(app, text="9", padx=40, pady=20,command=lambda:take_input("9"))

dot = tk.Button(app, text=".", padx=40, pady=20,command=lambda:take_input("."))
equal = tk.Button(app, text="=", padx=40, pady=20,command=equal_value)
plush = tk.Button(app, text="+", padx=40, pady=20,command=lambda:take_input("+"))
minus = tk.Button(app, text="-", padx=40, pady=20,command=lambda:take_input("-"))
multiply = tk.Button(app, text="*", padx=40, pady=20,command=lambda:take_input("*"))
divide = tk.Button(app, text="/", padx=40, pady=20,command=lambda:take_input("/"))
clear = tk.Button(app, text="C", padx=38, pady=20,command=clear_value)
percentage1= tk.Button(app, text="%", padx=38, pady=20,command=percentage)
back_space1=tk.Button(app, text="<--", padx=38, pady=20,command=back_space)
square_button=tk.Button(app, text="x^2", padx=38, pady=20,command=lambda:take_input("**"))

clear.grid(row=1,column=0)
square_button.grid(row=1,column=1)
percentage1.grid(row=1,column=2)
back_space1.grid(row=1,column=3)

seven.grid(row=2,column=0)
eight.grid(row=2,column=1)
nine.grid(row=2,column=2)
plush.grid(row=2,column=3)

four.grid(row=3,column=0)
five.grid(row=3,column=1)
six.grid(row=3,column=2)
minus.grid(row=3,column=3)

one.grid(row=4,column=0)
two.grid(row=4,column=1)
three.grid(row=4,column=2)
multiply.grid(row=4,column=3)

zero.grid(row=5,column=1)
dot.grid(row=5,column=2)
equal.grid(row=5,column=3)
divide.grid(row=5,column=0)



app.mainloop()




