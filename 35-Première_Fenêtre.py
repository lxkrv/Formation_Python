#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

import pygame

"""
pygame.FULLSCREEN   #Plein écran
pygame.RESIZABLE    #Redimensionne
pygame.NOFRAME      #supprime le cadre, plus de boutton (croix, diminution...)

pygame.OPENGL       #permet de travailler sur du rendu OPENGL
pygame.HWSURFACE    #Accélération logicielle
pygame.DOUBLEBUF    #Double mémoire tampon, pour éviter cassure lors d'affichage d'animation à l'écran, à utiliser si on utilise OPENGL ou HWSURFACE

"""


res = (640,480)
pygame.init() #trés important, sinon on peut psa charger les modules

pygame.display.set_caption("Ma fenêtre PYGAME")
window_surface = pygame.display.set_mode(res) #affiche une surface, ce qui va créer une fenêtre

#print(pygame.display.Info()) #affiche les informations de la fenêtre
#print(pygame.get_sdl_version()) #affiche la version 


launched = True
while launched:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False
        #res = (500,500)
        #window_surface = pygame.display.set_mode(res) #on peut redimensionner en cours

#pygame.quit() #pour décharger tous les modules qui ont été chargé avec le module init (très rare)