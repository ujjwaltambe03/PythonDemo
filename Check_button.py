#A Check Button is a GUI widget that presents to the user a set of predefined options in the form of boxes.
# The user is allowed to select more than one available option.

# syntax: ChkButton = Checkbutton(master, option.........)
# A Check Button returns 1 if it’s checked, otherwise it returns 0.

from tkinter import *

def Retreive_data():
    var2.set(var1.get())
    var4.set(var3.get())

root = Tk()
root.geometry("480x320")

frame = Frame (root )
frame.pack()

var1 ,var3 = IntVar() , IntVar()
var2, var4= StringVar() , StringVar()

check_button1 = Checkbutton (frame, text = "Option 1",variable = var1)
check_button1.pack()

check_button2 = Checkbutton (frame, text = "Option 2",variable = var3)
check_button2.pack()

# label to print which option choosed
label = Label(frame, textvariable= var2, width = 5, bg = 'grey')
label.pack()

label = Label(frame, textvariable= var4, width = 5, bg = 'grey')
label.pack()
# submit button to submit selected option
Sub_button = Button (frame, text = "Submit", command = Retreive_data)
Sub_button.pack()

root.mainloop()