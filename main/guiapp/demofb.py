import tkinter as tk

app = tk.Tk()
app.title="sample FB"
app.geometry("320x480")
app.config(bg='#003366')

label_username = tk.Label(app, text="Username")
label_username.pack()
entry_username = tk.Entry(app)
entry_username.pack()

label_password = tk.Label(app, text="Password")
label_password.pack()
entry_password = tk.Entry(app, show='*')
entry_password.pack()

button_sign_in = tk.Button( text="Sign In")
button_sign_in.pack()

app.mainloop()


