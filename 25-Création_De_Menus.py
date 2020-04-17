#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")

import tkinter

#add_checbutton()
#add_radiobutton()
#add_separator()

def hello():
    print("Hello!")

def show_about():
    about_window = tkinter.Toplevel(app)
    about_window.title("A propos...")
    lb = tkinter.Label(about_window, text = "Bonjour!")
    lb.pack()


#Création et paramètrage de la fenêtre
app = tkinter.Tk()
app.geometry("640x480")
app.title("Création de menus")



#widgets
mainmenu = tkinter.Menu()
first_menu = tkinter.Menu(mainmenu, tearoff=0) #tearoff permet de supprimer le séparateur dans la cascade du menu
first_menu.add_command(label = "Option1", command = hello)
first_menu.add_command(label = "A propos",command = show_about)
first_menu.add_separator()
first_menu.add_command(label = "Quitter", command = app.quit)

second_menu  = tkinter.Menu(mainmenu)
second_menu.add_command(label = "Commande1")
second_menu.add_command(label = "Commande2")
second_menu.add_command(label = "Commande3")

mainmenu.add_cascade(label="Premier", menu=first_menu)

mainmenu.add_cascade(label="Second", menu=second_menu)
#Boucle principale
app.config(menu=mainmenu)
app.mainloop()
