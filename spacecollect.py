import pygame
import time
import random



pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('collecting space coins')

Border = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)


collect_sound = pygame.mixer.Sound("Aerospace/collect.wav")


collected_total_font = pygame.font.SysFont("comicsans",40)
winner_font = pygame.font.SysFont("comicsans",100)

FPS = 60
VEL = 5
MAX_COINS = 3

SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40


RED_COLLECT = pygame.USEREVENT +1
YELLOW_COLLECT = pygame.USEREVENT +2

SPACESHIP_IMAGE = pygame.image.load("Aerospace/spaceship_1-removebg-preview.png")
SPACESHIP = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

SPACESHIP_IMAGE2 = pygame.image.load("Aerospace/spaceship_2-removebg-preview.png")
SPACESHIP2 = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMAGE2,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

coin_image = pygame.image.load("Aerospace/coin.png")
coin_image = pygame.transform.scale(coin_image,(20,20))

space = pygame.transform.scale(pygame.image.load("Aerospace/spacebg.jpg"),(WIDTH,HEIGHT))


def draw_window(red,yellow,coins,red_coins,yellow_coins,red_total_coins,yellow_total_coins):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"black",Border)

    red_total_coins =  collected_total_font.render("Health: "+str(red_total_coins),True,"white")
    yellow_total_coins = collected_total_font.render("Health: "+str(yellow_total_coins),True,"white")
    screen.blit(red_total_coins,(WIDTH - red_total_coins.get_width() - 10,10))
    screen.blit(yellow_total_coins,(10,10))
    screen.blit(SPACESHIP,(red.x,red.y))
    screen.blit(SPACESHIP2,(yellow.x,yellow.y))

    for coin in coins:
        screen.blit(coin_image,(coin.x,coin.y))

    pygame.display.update()


def yellow_handle_movement(key_pressed,yellow):
    if key_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
        yellow.x -= VEL
    if key_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < Border.x: #right
        yellow.x += VEL
    if key_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
        yellow.y -= VEL
    if key_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: #down
        yellow.y += VEL

        
def red_handle_movement(key_pressed,red):
    if key_pressed[pygame.K_LEFT] and red.x - VEL > Border.x + Border.width: #left
        red.x -= VEL
    if key_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #right
        red.x += VEL
    if key_pressed[pygame.K_UP] and red.y - VEL > 0: #up
        red.y -= VEL
    if key_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: #down
        red.y += VEL

def draw_winner(text):
    draw_text = winner_font.render(text,1,"white")
    screen.blit(draw_text,(WIDTH//2 - draw_text.get_width()//2,HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)

def handle_coins(red,yellow,coins,red_coins,yellow_coins):
    for coin in coins[:]:
        if red.colliderect(coin):
            pygame.event.post(pygame.event.Event(RED_COLLECT))
            coins.remove(coin)
            red_coins.append(coin)
            collect_sound.play()
        elif yellow.colliderect(coin):
            pygame.event.post(pygame.event.Event(YELLOW_COLLECT))
            coins.remove(coin)
            yellow_coins.append(coin)
            collect_sound.play()


def main():
    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    red_coins = []
    yellow_coins = []
    red_total_coins = 0
    yellow_total_coins = 0
    
    clock = pygame.time.Clock()

    run =  True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        for coins in range(MAX_COINS - len(red_coins) - len(yellow_coins)):
            coin_x = random.randint(0,WIDTH-20)
            coin_y = random.randint(0,HEIGHT-20)
            coin_rect = pygame.Rect(coin_x,coin_y,20,20)
            coins.append(coin_rect)


            if event.type == RED_COLLECT:
                red_total_coins += 1
                collect_sound.play()

            if event.type == YELLOW_COLLECT:
                yellow_total_coins += 1
                collect_sound.play()

        winner_text =  ""
        if red_total_coins >= 10:
            winner_text = "Red Wins!"
        if yellow_total_coins >= 10:
            winner_text = "Yellow Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            break        


        key_pressed = pygame.key.get_pressed()
        yellow_handle_movement(key_pressed,yellow)
        red_handle_movement(key_pressed,red)
        draw_window(red,yellow,coins,red_coins,yellow_coins,red_total_coins,yellow_total_coins)


    pygame.quit()

if  __name__ == "__main__":
    main()






















