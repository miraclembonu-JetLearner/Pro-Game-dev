import pygame
import time


pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('space shooting')

Border = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

bullet_sound = pygame.mixer.Sound("Aerospace/spacefire.wav")
Hit_sound = pygame.mixer.Sound("Aerospace/spacefireimpact.mp3")

health_font = pygame.font.SysFont("comicsans",40)
winner_font = pygame.font.SysFont("comicsans",100)


FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3

SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40

SPACESHIP_HIT = pygame.USEREVENT +1
SPACESHIP_FIRE = pygame.USEREVENT +2

SPACESHIP_IMAGE = pygame.image.load("Aerospace/spaceship_1-removebg-preview.png")
SPACESHIP = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

SPACESHIP_IMAGE2 = pygame.image.load("Aerospace/spaceship_2-removebg-preview.png")
SPACESHIP2 = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMAGE2,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

space = pygame.transform.scale(pygame.image.load("Aerospace/spacebg.jpg"),(WIDTH,HEIGHT))

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"black",Border)

    red_health =  health_font.render("Health: "+str(red_health),1,"white")
    yellow_health = health_font.render("Health: "+str(yellow_health),1,"white")
    screen.blit(red_health(WIDTH - red_health.get_width() - 10,10))
    screen.blit(yellow_health(10,10))
    screen.blit(SPACESHIP,(red.x,red.y))

    screen.blit(SPACESHIP2,(yellow.x,yellow.y))
    for bullet in red_bullets:
        pygame.draw.rect(screen,"red",bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(screen,"yellow",bullet)

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


def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SPACESHIP_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SPACESHIP_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = winner_font.render(text,1,"white")
    screen.blit(draw_text,(WIDTH//2 - draw_text.get_width()//2,HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []
    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()

    run =  True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.quit:
                run = False
                pygame.quit()
            
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width,yellow.y + yellow.height//2 - 2,10,5)
                    yellow_bullets.append(bullet)
                    bullet_sound.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x,red.y + red.height//2 - 2,10,5)
                    red_bullets.append(bullet)
                    bullet_sound.play()
            if event.type == SPACESHIP_HIT:
                red_health -= 1
                Hit_sound.play()

            if event.type == SPACESHIP_HIT:
                yellow_health -= 1
                Hit_sound.play()

        winner_text =  ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        if yellow_health <= 0:
            winner_text = "Red Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            break

        key_pressed = pygame.key.get_pressed()
        yellow_handle_movement(key_pressed,yellow)
        red_handle_movement(key_pressed,red)
        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)
    
    main()

if  __name__ == "__main__":
    main()
