# This widget is used to get the text data from user via GUI
# A simple box is provided on the interface where the user can input text.
# This text can then be retrieved and used by us through the use special functions.

# syntax: Entry = Entry(master, option.........)

# program takes a input data from entry widget and clicked button to take action specified.
# In this after clicking button we are showing the same data in labels

from tkinter import *

def retrieve_data():
    var.set(entry_1.get())

root = Tk()
root.geometry("480x340")

frame = Frame(root)
frame.pack()

# creating entry to take input
entry_1 = Entry(frame, width = 15)
entry_1.insert(50,'Give Input')  # insert is use to store provided string at 0 index
entry_1.pack(padx = 10 , pady =10)

var = StringVar()
var.set("   ")

label = Label(frame, textvariable= var, width = 15, fg = "black", bg ='grey')
label.pack()  # without pack function widget won't get displayed

# creating button to perform some action
button = Button(frame, text = "Submit", command = retrieve_data)
button.pack()

root.mainloop()