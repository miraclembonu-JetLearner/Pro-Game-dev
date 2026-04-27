import pygame
import time

pygame.init()

WIDTH = 500
HEIGHT = 500

display_surface = pygame.display.set_mode((WIDTH,HEIGHT))


pygame.display.set_caption("Birthday card")

img = pygame.image.load("Birthday animation/birthday-1.jpg")

img_1 = pygame.transform.scale(img,(WIDTH,HEIGHT))

while(True):
    for event in pygame .event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    display_surface.blit(img_1,(0,0))
    font = pygame .font.SysFont("ALGERIA",50)
    text = font.render("Happy Birthday",True,"blue")
    display_surface.blit(text,(200,200))
    pygame.display.update()