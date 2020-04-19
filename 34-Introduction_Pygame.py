#coding:utf-8
import os
import time
# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))

launched = True

while launched:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False