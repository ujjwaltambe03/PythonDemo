# A radio button is a widget that allows the user to choose only one of a predefined options.
# syntax : Rbttn = Radiobutton(master, option..........)

from tkinter import *

def Retreive_data():
    var2.set(var1.get())

root = Tk()
root.geometry("480x340")

var1 = IntVar()
var2 = StringVar()

Rad_Button_1 = Radiobutton(root, text = "Option_1", variable = var1,value = 1)
Rad_Button_1.pack()

Rad_Button_2 = Radiobutton(root, text = "Option_2", variable = var1,value = 2)
Rad_Button_2.pack()


label = Label(root, textvariable= var2, width = 10, bg = 'grey')
label.pack()

Sub_button = Button (root, text = "Submit", command = Retreive_data)
Sub_button.pack()

root.mainloop()