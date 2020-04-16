#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")

import tkinter
#from tkinter import *

mainapp = tkinter.Tk() #Constructeur pour créer la fenêtre (qui s'appelle un widget)
mainapp.title("Mon premier programme fenêtré")
"""
mainapp.minsize(640,480)                    #Taille minimale
mainapp.maxsize(1280,720)                   #Taille maximale
mainapp.geometry("800x600")                 #Taile de la fenêtre qui reste modifiable à l'affichage

mainapp.resizable(width=False, height=True) #Pour autoriser le redimenso=ionnement  
mainapp.positionfrom("user")                #Positionner la fenêtre
mainapp.sizefrom("user")
"""
#mainapp.geometry("800x600+50+50") #Pour positionner la taille et place la fenêtre en haut à gauche à 50,50

#position_X = (largeur_ecran//2) - (largeur_fenêtre//2)
#position_Y = (hauteur_ecran//2) - (hauteyr_fenêtre//2)

screen_x = mainapp.winfo_screenwidth()
screen_y = mainapp.winfo_screenheight()

window_x = 800
window_y = 600

position_X = (screen_x//2) - (window_x//2)
position_Y = (screen_y//2) - (window_y//2)

geo = "{}x{}+{}+{}".format(window_x, window_y,position_X,position_Y)

mainapp.geometry(geo)

mainapp.mainloop()
#mainapp.quit() méthode pour quitter la fenêtre, là on va la fermer avec la croix 