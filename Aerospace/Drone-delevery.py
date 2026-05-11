import pygame

pygame.init()


WIDTH = 400
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH,HEIGHT))


pygame.display.set_caption("delevery drone")



player_x = 200
player_y = 200


player_x = pygame.image.load("Aerospace/Drone-removebg-preview.png")
background = pygame.image.load("Aerospace/Bright-setting.jpg")



key = [False,False,False,False]

while player_x < 600:
    screen.blit(background,(0,0))
    screen.blit(player_x,(player_x,player_y))

    for event in pygame .event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                key[0] = True
            elif event.key == pygame.K_RIGHT:
                key[1] = True
            elif event.key == pygame.K_UP:
                key[2] = True
            elif event.key == pygame.K_DOWN:
                key[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                key[0] = False
            elif event.key == pygame.K_RIGHT:
                key[1] = False
            elif event.key == pygame.K_UP:
                key[2] = False
            elif event.key == pygame.K_DOWN:
                key[3] = False
    