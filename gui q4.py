from tkinter import *


import tkSimpleDialog
import tkMessageBox

root=Tk()

w=label(root,text="my program")
w.pack()


tkMessageBox.showinfo("welcome","aadd detail")
 
name=tkSimpleDialog.askstring("name","what is your nmame")
name.pack()
age=tkSimpleDialog.askinteger("age","how old are yoy")
age.pack()

root.mainloop()
