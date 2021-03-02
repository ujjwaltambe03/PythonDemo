# The Python Tkinter Combobox presents a drop down list of options and displays them one at a time.
# The Python Combobox is actually a sub class of the widget Entry.
# You must specially import the ttk module to be able to use Comboboxes.
# from tkinter import ttk
# Combo = ttk.Combobox(master, values.......)

from tkinter import *
from tkinter import ttk

def execute():
    #print(combo.get())
    if combo.get() == lst[0]:
        print("opt 1 selected")
    elif combo.get() == lst[1]:
        print("opt 2 selected")
    elif combo.get() == lst[2]:
        print("opt 3 selected")
    elif combo.get() == lst[3]:
        print("opt 4 selected")
    elif combo.get() == lst[4]:
        print("opt 5 selected")

root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()

lst = ["DiagnosticSessionService", "ECUReset", "RequestDownload",
         "TransferData", "RequestExit"]

combo = ttk.Combobox(frame, values = lst)
combo.set("pick an option")
combo.pack()

button = Button(frame, text= "submit", command = execute)
button.pack()

root.mainloop()