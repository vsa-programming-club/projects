import pygame, sys, time
from pygame.locals import *

windowSurface = pygame.display.set_mode((400,400),0,32)
pygame.display.set_caption('animation')

image = pygame.image.load('smiley.png')
background = pygame.image.load('background.jpg')

rect = pygame.Rect(300, 80, 40, 40)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                rect.x -= 5
            elif event.key == K_RIGHT:
                rect.x += 5
            elif event.key == K_UP:
                rect.y -= 5
            elif event.key == K_DOWN:
                rect.y += 5

    #windowSurface.fill((121,214,52))
    windowSurface.blit(background, pygame.Rect(0,0,400,400))

    #pygame.draw.rect(windowSurface, (255,0,0), rect)
    windowSurface.blit(image, rect)

    pygame.display.update()
    time.sleep(0.02)
