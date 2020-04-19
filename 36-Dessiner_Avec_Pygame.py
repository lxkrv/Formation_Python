#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

import pygame
pygame.init()

#objet : Surface, Rect
#Rect(left,top, width, height)

window_resolution = [600, 480]
blue_color = (89, 152, 255)
black_color = (0,0,0)
window_surface = pygame.display.set_mode(window_resolution)
window_surface.fill(blue_color) #ca ne remplit pas encore en bleu

pygame.draw.line(window_surface, black_color,[10,10],[200,200])
rectangle = pygame.Rect(50,50,75,100)
pygame.draw.circle(window_surface, black_color, [320, 100], 45, 4) 
pygame.draw.rect(window_surface, black_color,rectangle) 
coords = [(200,200),(200,220),(230,250)]
pygame.draw.polygon(window_surface, black_color, coords, 3)


pygame.display.flip() #mis à jour de l'affichage


launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

