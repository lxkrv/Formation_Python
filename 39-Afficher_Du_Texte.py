#coding:utf-8
import os
import time

# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

import pygame
pygame.init()
window_resolution = [640, 480]
blue_color = (0, 75, 255)

pygame.display.set_caption("Python #37")

window_surface = pygame.display.set_mode(window_resolution)
arial_font = pygame.font.SysFont("arial", 20)
helllo_text = arial_font.render("Hello World !$£#%", False, blue_color)
window_surface.blit(helllo_text,[10,10])
pygame.display.flip()


#print(pygame.font.get_fonts()) #affiche toute la liste des polics de caractères utilisés dans le pc 


launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    #Corps du programme
