# Tkinter works with a hierarchical system, where there is one root window from where all other widgets and windows expand from.
# Calling the Tk() function initializes the whole Tkinter application.
# Often while creating a GUI, you wish to have more than just one window.
# Instead of calling the Tk() function again you should use the Tkinter Toplevel widget instead.

# Calling the Tk() function creates a whole Tkinter instance, while calling the Toplevel() function only creates a window under the root Tkinter instance.
# Destroying the Tk() function instance will destroy the whole GUI,
# whereas destroying the Toplevel() function only destroys that window and it’s child widgets,
# but not the whole program.

# syntax: window = Toplevel(options.....)

from tkinter import *


def NewWindow():
    window = Toplevel()
    window.geometry('150x150')
    newlabel = Label(window, text="Settings Window")
    newlabel.pack()


root = Tk()
root.geometry('200x200')

myframe = Frame(root)
myframe.pack()

mybutton = Button(myframe, text="Settings", command=NewWindow)
mybutton.pack(pady=10)

root.mainloop()