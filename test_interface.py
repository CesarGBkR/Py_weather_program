from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("800x600")
frm = ttk.Frame(root, padding=200)
frm.grid()

# Style
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

# Elements

# Entry
ttk.Label(frm, text='Search your country:').grid(column=1, row=0)
nombre=StringVar()
nomb=ttk.Entry(frm, textvariable=nombre).grid(column=1, row=1)
# Buttons
ttk.Button(frm, text="Search", command=root.quit).grid(column=0, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=2)

root.title("API Call") # Title
root.mainloop()
