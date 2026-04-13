import pygame
pygame.init()

windows = pygame.display.set_mode((400,400))


pygame.draw.circle(windows,"red",(100,150),40,3)

pygame.draw.circle(windows,"red",(200,250),40)

pygame.display.update()


run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
