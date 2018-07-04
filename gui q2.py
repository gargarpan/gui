from tkinter import *

root = Tk()

hwL = Label(root, text='Hello World!!')

hwL.pack()

def clicked():
    hwL.configure(text="button was clicked")

    
submitB = Button(root, text='Submit', bg='green',\
                 command=clicked)

submitB.pack()
exitB = Button(root, text='exit', width=25, \
               command=root.destroy)

exitB.pack()

root.mainloop()

