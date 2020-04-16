#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")

"""
showerror
showwarning
showinfo
askquestion
askokcancel
askretrycancel
"""


import tkinter
from tkinter import messagebox
app = tkinter.Tk()

def show_modal_windows():
    messagebox.showerror("Erreur", "un problème est survenu!")

btm = tkinter.Button(app, text="Déclencher une erreur", command = show_modal_windows)

check_widget = tkinter.Checkbutton(app, text = "Publier?", offvalue = 2, onvalue = 5, height = 10, width = 10)
radio_widget1 = tkinter.Radiobutton(app, text = "Homme", value = 1)
radio_widget2 = tkinter.Radiobutton(app, text = "Femme", value = 0 )
scale_widget = tkinter.Scale(app, from_=0, to=100, tickinterval = 25)
spin_widget = tkinter.Spinbox(app, from_=1, to=10)
list_box = tkinter.Listbox(app)
list_box.insert(1,"Windows")
list_box.insert(2,"Linux")
list_box.insert(3,"MacOS")

btm.pack()
check_widget.pack()
radio_widget1.pack()
radio_widget2.pack()
scale_widget.pack()
spin_widget.pack()
list_box.pack()
app.mainloop()