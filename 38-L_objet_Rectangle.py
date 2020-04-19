#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

import pygame
import time
"""
pygame.Rect(x, y, width, height)
mynewrect = myrect.copy()
Rect.move()  ou Rect.move_in_place() --> déplacement réel
Rect.inflate() #agrandir ou rétrécir le rectangle
Rect.colliderect() #détecte la collision

"""

pygame.init()
window_resolution = [640, 480]
red_color = (255, 0, 0)
black_color = (0, 0, 0)
blue_color = (0, 75, 255)
i = 0

pygame.display.set_caption("Python 38 - l'objet Rect")
window_surface = pygame.display.set_mode(window_resolution)

myrect = pygame.Rect(10,100,25,25)
my_block = pygame.Rect(600, 50, 20, 300)

pygame.draw.rect(window_surface, red_color, myrect)
pygame.draw.rect(window_surface, blue_color, my_block)
pygame.display.flip()


"""
while i < 10:
    time.sleep(0.05)
    window_surface.fill(black_color)
    pygame.draw.rect(window_surface, red_color, myrect)
    pygame.display.flip()
    myrect.x += 10
    myrect.y += 10
    i += 1
"""



launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

    while not myrect.colliderect(my_block):
        time.sleep(0.01)
        window_surface.fill(black_color)
        myrect.x += 1
        pygame.draw.rect(window_surface, red_color, myrect) #--> renvoie un Rect
        pygame.draw.rect(window_surface, blue_color, my_block)
        pygame.display.flip()