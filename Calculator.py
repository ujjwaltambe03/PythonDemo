from tkinter import *

root = Tk()  # creating an object from Tk()
root.geometry("480x420")  # setting the geometry of the GUI

frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

label = Label(frame, text="Demo", bg= 'red')
label.pack()

def print_data():
    print("you clicked button")

button_1 = Button(leftframe, text="Button1",fg= 'Red', command = print_data)
button_1.pack(padx = 100, pady = 100)
button_2 = Button(rightframe, text="Button2")
button_2.pack(padx = 20, pady = 20)
button_3 = Button(leftframe, text="Button3")
button_3.pack(padx = 30, pady = 30)

root.title("Calculator")  # title
root.mainloop()  # running loop
