
from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

# Style
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

# Elements
# ttk.Label(frm,text="Style test", style="BW.TLabel").grid(column=2, row=0) # Using Style
# Elements without style
ttk.Label(frm, text="API Search").grid(column=1, row=0)
ttk.Button(frm, text="Search", command=root.destroy).grid(column=0, row=1)
# ttk.Label(frm, text="Colum 1").grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=1)

ttk.Combobox(frm, text="Combobox").grid(column=3, row=1)

# ttk.Label(frm,text="Style test",foreground="black", background="white").grid(column=3, row=0) # Explicit Style

root.title("API Call") # Title
root.mainloop()
