import pygame
pygame.init()

done = False

windows = pygame.display.set_mode((400,400))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        pygame.draw.rect(windows,"red",pygame.Rect(100,100,50,50))

        pygame.draw.rect(windows,"blue",pygame.Rect(200,150,150,150))

    pygame.display.update()

