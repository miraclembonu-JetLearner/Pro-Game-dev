import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

# Window
WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect Falling Coins")

# Fonts
font = pygame.font.SysFont("comicsans", 40)
title_font = pygame.font.SysFont("comicsans", 60)
game_over_font = pygame.font.SysFont("comicsans", 80)

# Sounds
collect_sound = pygame.mixer.Sound("Aerospace/collect.wav")

# Images
SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40

SPACESHIP_IMAGE = pygame.image.load("Aerospace/spaceship_1-removebg-preview.png")
spaceship_img = pygame.transform.rotate(
    pygame.transform.scale(SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    90
)

bomb_image = pygame.image.load("Aerospace/bomb.png")
bomb_image = pygame.transform.scale(bomb_image, (20, 20))

coin_image = pygame.image.load("Aerospace/coin.png")
coin_image = pygame.transform.scale(coin_image, (20, 20))

space_bg = pygame.transform.scale(
    pygame.image.load("Aerospace/spacebg.jpg"),
    (WIDTH, HEIGHT)
)

clock = pygame.time.Clock()

# Game variables
coins = []
bombs = []
score = 0
coin_timer = 0
bomb_timer = 0
coin_speed = 5
bomb_speed = 7
game_over = False

# Spaceship Rect
spaceship = spaceship_img.get_rect()
spaceship.x = WIDTH // 2
spaceship.y = HEIGHT - 80


def create_coin():
    x = random.randint(0, WIDTH - 20)
    y = -20
    return pygame.Rect(x, y, 20, 20)

def create_bomb():
    x = random.randint(0, WIDTH - 20)
    y = -20
    return pygame.Rect(x, y, 20, 20)

def move_spaceship(keys):
    if keys[pygame.K_LEFT] and spaceship.x > 0:
        spaceship.x -= 6
    if keys[pygame.K_RIGHT] and spaceship.x + spaceship.width < WIDTH:
        spaceship.x += 6


def move_coins():
    global coin_speed
    for coin in coins:
        coin.y += coin_speed

def move_bombs():
    global bomb_speed
    for bomb in bombs:
        bomb.y += bomb_speed

def remove_offscreen_coins():
    for coin in coins[:]:
        if coin.y > HEIGHT:
            coins.remove(coin)

def remove_offscreen_bombs():
    for bomb in bombs[:]:
        if bomb.y > HEIGHT:
            bombs.remove(bomb)

def check_coin_collision():
    global score
    for coin in coins[:]:
        if spaceship.colliderect(coin):
            coins.remove(coin)
            score += 1
            collect_sound.play()

def check_bomb_collision():
    global game_over
    for bomb in bombs[:]:
        if spaceship.colliderect(bomb):
            game_over = True

def draw_window():
    screen.blit(space_bg, (0, 0))
    screen.blit(spaceship_img, (spaceship.x, spaceship.y))

    for coin in coins:
        screen.blit(coin_image, (coin.x, coin.y))

    for bomb in bombs:
        screen.blit(bomb_image, (bomb.x, bomb.y))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    title_text = title_font.render("Collect Falling Coins", True, (100, 155, 250))
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))


def draw_game_over():
    screen.blit(space_bg, (0, 0))

    over_text = game_over_font.render("GAME OVER", True, (255, 50, 50))
    screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 80))

    score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))

    restart_text = font.render("Press R to Restart", True, (200, 200, 200))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 60))


def reset_game():
    global coins, score, coin_timer, coin_speed, game_over , bombs , bomb_speed
    bombs = []
    coins = []
    score = 0
    coin_timer = 0
    coin_speed = 5
    bomb_speed = 7
    game_over = False
    spaceship.x = WIDTH // 2
    spaceship.y = HEIGHT - 80


# Main loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:
        coin_timer += 1
        bomb_timer += 1

        # Difficulty scaling
        if score % 10 == 0 and score != 0:
            coin_speed = 5 + (score // 10)
            bomb_speed = 7 + (score // 10)
            
        if coin_timer >= 30:
            coins.append(create_coin())
            coin_timer = 0

        if bomb_timer >= 60:
            bombs.append(create_bomb())
            bomb_timer = 0

        move_spaceship(keys)
        move_coins()
        move_bombs()
        remove_offscreen_coins()
        remove_offscreen_bombs()
        check_coin_collision()
        check_bomb_collision()

        draw_window()

        # End game if too many coins fall
        if len(coins) > 25:
            game_over = True

    else:
        draw_game_over()
        if keys[pygame.K_r]:
            reset_game()

    pygame.display.update()

pygame.quit()
sys.exit()
