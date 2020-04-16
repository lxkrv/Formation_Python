#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")


import tkinter

#observateur
def udpate_observer(*args):
    print(f"J'ai vu !, Sexe : {var_gender.get()}") #Evite d'utiliser le if = 1-> homme, 0--> femme
    if var_gender.get():
        print("c'est une homme")
        var_label_gender.set("C'est un homme")

    else:
        print("c'est une femme")
        var_label_gender.set("C'est une femme")


#Création et paramètrage de la fenêtre
app = tkinter.Tk()
app.geometry("400x300")
app.title("Variables Tkinter")

#Widgets
var_gender = tkinter.IntVar()
var_gender.trace("w", udpate_observer)
radio1 = tkinter.Radiobutton(app, value=1, text="Homme", variable = var_gender)
radio2 = tkinter.Radiobutton(app, value=0, text="Femme", variable = var_gender) 

var_label_gender = tkinter.StringVar()
label_gender = tkinter.Label(app, textvariable = var_label_gender)

radio1.pack()
radio2.pack()
label_gender.pack()
#Programme principal
app.mainloop()