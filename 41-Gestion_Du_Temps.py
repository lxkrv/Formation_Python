#coding:utf-8
import os
import time

# for windows
os.system('cls')
#os.system("ls")
time.sleep(0.5)

import pygame

window_resolution = [640, 480]
blue_color = (132, 180, 255)
red_color = (255, 0, 0)
black_color = (0, 0, 0)
launched = True

pygame.init()

clock = pygame.time.Clock()

pygame.time.set_timer(pygame.USEREVENT, 2000)

pygame.display.set_caption("Python #41 - Mesurer le temps")
window_surface = pygame.display.set_mode(window_resolution)
arial_font = pygame.font.SysFont("arial", 36)
text = arial_font.render("Hello World", True, blue_color)
window_surface.blit(text, [50,50])
pygame.display.flip()

#pygame.time.wait(2000)
#pygame.time.delay(2000) #c'est le processeur qui gèle le programme

text = arial_font.render("Hello World", True, red_color)
arial_font = pygame.font.SysFont("arial", 36)


window_surface.blit(text, [50,50])
pygame.display.flip()

print(pygame.time.get_ticks())

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.USEREVENT:
            window_surface.fill(black_color)
            text1 = arial_font.render(f"FPS : {clock.get_fps():.2f}", True, blue_color)
            window_surface.blit(text1, [100,100])
            pygame.display.flip()
    
    clock.tick(60)
 
    #text = arial_font.render("Hello World", True, red_color)
    arial_font = pygame.font.SysFont("arial", 36)
    
    print(f"FPS : {clock.get_fps()}")
    #print("%.2f" % clock.get_fps())
    #print(f"{clock.get_fps()}:.f")    