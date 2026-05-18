import pygame

pygame.init()


WIDTH = 400
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH,HEIGHT))


pygame.display.set_caption("delevery drone")



player_x = 200
player_y = 200


player = pygame.image.load("Aerospace/drone.png")
player = pygame.transform.scale(player,(50,50))
background = pygame.image.load("Aerospace/BG.jpg")



key = [False,False,False,False]

while True:
    screen.blit(background,(0,0))
    screen.blit(player,(player_x,player_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                key[0] = True
            elif event.key == pygame.K_LEFT:
                key[1] = True
            elif event.key == pygame.K_DOWN:
                key[2] = True
            elif event.key == pygame.K_RIGHT:
                key[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                key[0] = False
            elif event.key == pygame.K_LEFT:
                key[1] = False
            elif event.key == pygame.K_DOWN:
                key[2] = False
            elif event.key == pygame.K_RIGHT:
                key[3] = False

        if key[0]:
            if player_y > 0:
                player_y -=10
        elif key[2]:
            if player_y < 350:
                player_y +=10
        elif key[1]:
            if player_x > 0:
                player_x -=10
        elif key[3]:
            if player_x < 350:
                player_x +=10

    pygame.display.update()
