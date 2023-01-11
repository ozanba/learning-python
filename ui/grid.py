from tkinter import *
root = Tk()
#creating label
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Ozan Bagiran")
#shoving label on to screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
root.mainloop()