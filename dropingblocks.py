import pygame
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Avoid falling blocks')

font = pygame.font.SysFont("comicsans", 50)

BLACK = (0, 0, 0)
BLUE = (50, 50, 100)
RED = (255, 50, 50)

blocks = []
score = 0

block_speed = 5
block_width = 50
block_height = 50
block_timer = 0

clock = pygame.time.Clock()


player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 100, 50, 10)


def draw_window(player, blocks, score):
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, player)
    for block in blocks:
        pygame.draw.rect(screen, RED, block)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 50))


def create_block():
    x = random.randint(0, WIDTH - block_width)
    y = -block_height
    block = pygame.Rect(x, y, block_width, block_height)
    blocks.append(block)


def move_player(player, keys):
    if keys[pygame.K_LEFT] and player.x - 5 > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x + player.width + 5 < WIDTH:
        player.x += 5


def move_blocks():
    for block in blocks:
        block.y += block_speed


def check_player_collision(player):
    for block in blocks:
        if player.colliderect(block):
            return True
    return False


def remove_offscreen_blocks():
    global score
    for block in blocks[:]:
        if block.y > HEIGHT:
            blocks.remove(block)
            score += 1


running = True
while running:
    clock.tick(60)
    block_timer += 1

    if block_timer >= 30:
        create_block()
        block_timer = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    move_player(player, keys)
    move_blocks()
    remove_offscreen_blocks()

    if check_player_collision(player):
        running = False
        print("Game Over! Your score is:", score)

    draw_window(player, blocks, score)
    pygame.display.update()

pygame.quit()
sys.exit()
