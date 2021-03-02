# this example explains usage of button, lable
# Label is a widget which is use to show some text data
# button is an input to the GUI which will perform defined action.

from tkinter import *

def set_1():
    print("You clicked the button")
    var1.set(" clicked")

def set():
    var.set("Good-Bye Cruel World")  # can use input() to take directly data from user

root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()

button = Button(frame, text="Button1", command=set_1) # dont use parathesis with function name
button.pack()

var = StringVar()
var.set("Hello World")

var1 = StringVar()
var1.set("customized")

label = Label(frame, textvariable=var)
label.pack()

label = Label(frame, textvariable=var1)
label.pack()

button_1 = Button(frame, text="set", command=set)
button_1.pack()

root.mainloop()