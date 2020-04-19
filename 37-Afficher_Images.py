#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

import pygame
pygame.init()
window_resolution = [1000, 1000]
blanck_color  = (255,255,255)

pygame.display.set_caption("Python #37")
window_surface = pygame.display.set_mode(window_resolution)

cat_image = pygame.image.load("Python_Logo.jpg") #retourne une surface
cat_image.convert() #conertir pour avoir un affichaage plus performant (pour blit)

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    #Corps du programme
    window_surface.fill(blanck_color)
    window_surface.blit(cat_image, [40,40])
    pygame.display.flip()
