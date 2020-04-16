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
mainframe = tkinter.LabelFrame(app, width = 300, height = 200, borderwidth = 2, text="Titre") #Label permet de nommer le frame
mainframe.pack()

btn = tkinter.Button(mainframe , text = "Bienvenue!")
btn.pack()
#Bouucle principale
app.mainloop()