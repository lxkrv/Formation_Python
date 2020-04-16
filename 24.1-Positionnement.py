#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")

import tkinter

#Création et paramètrage de la fenêtre
app = tkinter.Tk()
app.geometry("400x300")
app.title("Variables Tkinter")

#widgets
label = tkinter.Label(app, text = "Un label")
ent = tkinter.Entry(app)
btn = tkinter.Button(app , text = "Bienvenue!")
"""

btn.pack(padx=100,fill="both") #par défaut dans le pack(side="top") , bottom, right et left pour le placement
ent.pack(side="left",fill="y")
label.pack(expand=1)
"""
label.grid(row=0, column=0, columnspan = 2, rowspan = 3)
ent.grid(row=0, column=2)
btn.grid(row=0, column=3)
#Bouucle principale
app.mainloop()