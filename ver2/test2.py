import tkinter as tk
from tkinter import *
from tkinter import ttk
root = tk.Tk()

root.geometry("900x900")
root.title("ending my life!!!!")

label = tk.Label(root, text="hiiiiiiii!!!!!", font=('Ariel', 18, 'bold', 'italic', 'underline'),fg="#b00b1e")
label.pack(padx=20, pady=20)
label.place(x=0,y=0)

textbox = tk.Text(root, height=3, font=('Arial', 16))

textbox.pack(padx=10, pady=10)
textbox.place(x=0,y=0)

root.mainloop()





