#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")

"""
StringVar() : chaîne de caractère [str]
IntVar()    : nombre entier [int]
DoubleVar() : nombre flottant [float]
BooleanVar(): booléen [bool]
"""

import tkinter

def udpate_label(*args):
    var_label.set(var_entry.get())



#Création et paramètrage de la fenêtre
app = tkinter.Tk()
app.geometry("400x300")
app.title("Variables Tkinter")

#Widgets
var_entry = tkinter.StringVar()
var_entry.trace("w",udpate_label) #le mode est entre ""

entry = tkinter.Entry(app, textvariable = var_entry)

var_label = tkinter.StringVar() #Création de la variable str avec StringVar
label = tkinter.Label(app, text="", textvariable = var_label)
var_label.set("Le label...")

entry.pack()
label.pack()

#var_label.set("Coucou")
print("Label : ", var_label.get())


#Programme principal
app.mainloop()