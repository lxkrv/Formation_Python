#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")

"""
<nom_variable> = <nom_widget>(<widget_parent>, <params>, ...)
label -->sur une ligne
message --> sur plusieurs lignes
"""
import tkinter
app = tkinter.Tk() #Création de la fenêtre

#label_welcome = tkinter.Label(app, text="Hello world !") #ligne seul n'affiche rien
label_welcome = tkinter.Message(app, text="Hello World! et bienvenue dans la matrice")

""" Différentes méthodes sur les widgets
print(label_welcome["text"])
print(label_welcome.cget("text"))

label_welcome.configure(text="nouveau message") #pour modifier le paramètre d'un widget
"""

entry_name = tkinter.Entry(app, width = 45, show="*") #width fixe la longueur de la fenetre de saisise, show pour un mot de passe
label_welcome.pack()
entry_name.pack()

def hello():
    print("Hello sur le Terminal!")

button_quit = tkinter.Button(app, text="OK",width = 25, height = 5, command = hello)
button_quit.pack()

app.mainloop() #Pour éviter la fermeture de la fenêtre

