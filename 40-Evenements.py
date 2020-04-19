#coding:utf-8
import os
import time

# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

import pygame




window_resolution = [640, 480]
white_color = (255, 255, 255)
black_color = (0, 0, 0)
pygame.init()
pygame.display.set_caption("Python #40 - Evénements")
window_surface = pygame.display.set_mode(window_resolution)

"""
arial_font = pygame.font.SysFont("arial",30)
dimensions_text = arial_font.render("{}".format(window_resolution), True, white_color)
window_surface.blit(dimensions_text,[10,10])
"""

pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("haut")
            elif event.key == pygame.K_DOWN:
                print("bas")
            elif event.key ==pygame.K_LEFT:
                print("gauche")
            elif event.key == pygame.K_RIGHT:
                print("droite")
            else :
                print("autre touche")
        if event.type == pygame.MOUSEMOTION:
            print("{}".format(event.pos))        
