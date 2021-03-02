# A radio button is a widget that allows the user to choose only one of a predefined options.
# syntax : Rbttn = Radiobutton(master, option..........)

from tkinter import *

def Retreive_data():
    var2.set(var1.get())

root = Tk()
root.geometry("480x340")

frame = Frame(root)
frame.pack()

var1 = IntVar()
var2 = StringVar()

# creating option 1 and 2
Rad_Button_1 = Radiobutton(frame, text = "Option_1", variable = var1,value = 1)
Rad_Button_1.pack()

Rad_Button_2 = Radiobutton(frame, text = "Option_2", variable = var1,value = 2)
Rad_Button_2.pack()

# label to print which option choosed
label = Label(frame, textvariable= var2, width = 10, bg = 'grey')
label.pack()

# submit button to submit selected option
Sub_button = Button (frame, text = "Submit", command = Retreive_data)
Sub_button.pack()

root.mainloop()