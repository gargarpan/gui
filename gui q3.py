# Working with Frames

from tkinter import *

root = Tk()

root.title('My App')

root.configure(background='blue')

frame_1 = Frame(root, bg='black')

frame_1.pack(fill=X)

frame_2 = Frame(root, bg='brown')

frame_2.pack(fill=X, side=BOTTOM)

lbl_1L = Label(frame_1, text='This is Label 1', bg='red')

lbl_1L.pack()

lbl_2L = Label(frame_2, text='This is Label 2', bg='white')

lbl_2L.pack()
def clicked():
    lbl_2L.configure(text="button was clicked")


submitB = Button(root, text='Submit', bg='green',\
                 activebackground='yellow', \
                 activeforeground='white',command=clicked)
submitB.pack()
exitB = Button(root, text='exit', width=25, \
               command=root.destroy)
exitB.pack()

root.mainloop()

# Change label container to root
