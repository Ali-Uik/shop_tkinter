from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Button(frm, text="Quit").grid(column=0, row=0)
root.mainloop()