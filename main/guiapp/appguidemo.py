import tkinter as tk

app= tk.Tk()
app.title("python")
app.geometry("400x500")

l1 = tk.Label(app,text="Enter a  first number")
l1.pack()
n1 = tk.Entry(app)
n1.pack()
l2 = tk.Label(app,text="Enter the Second Number")
l2.pack()
n2= tk.Entry(app)
n2.pack()

def add():
    x= int(n1.get())
    y=int(n2.get())
    res = x+y
    result.config(text="Result :"+str(res))


button= tk.Button(app,text=" SUM ",command=add)  
button.pack()
result = tk.Label(app,text="Result")
result.pack()



app.mainloop()