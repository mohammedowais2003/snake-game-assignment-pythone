
#  presentation link below   #,
#  https://drive.google.com/file/d/10uUz7GBpD3CiD86fEXA80W0bGwI0H0Ka/view?usp=sharing           #

import pygame
import random
import sys

pygame.init()

# Window
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Colors
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)

BLOCK = 20
font = pygame.font.SysFont(None, 30)

snake = [(100,100)]
direction = "RIGHT"

food = (random.randrange(0, WIDTH, BLOCK),
        random.randrange(0, HEIGHT, BLOCK))

score = 0
speed = 10
paused = False


def draw_text(text,x,y,color=WHITE):
    img = font.render(text,True,color)
    screen.blit(img,(x,y))


def move_snake():
    global food,score,speed

    x,y = snake[0]

    if direction=="RIGHT": x+=BLOCK
    if direction=="LEFT": x-=BLOCK
    if direction=="UP": y-=BLOCK
    if direction=="DOWN": y+=BLOCK

    new_head=(x,y)
    snake.insert(0,new_head)

    if new_head==food:
        score+=1
        speed+=0.5
        food=(random.randrange(0, WIDTH, BLOCK),
              random.randrange(0, HEIGHT, BLOCK))
    else:
        snake.pop()


def collision():
    head=snake[0]

    if head[0]<0 or head[0]>=WIDTH or head[1]<0 or head[1]>=HEIGHT:
        return True

    if head in snake[1:]:
        return True

    return False


def game_over():
    screen.fill(BLACK)
    draw_text("GAME OVER",230,150,RED)
    draw_text(f"Score: {score}",250,200)
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()


while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_p:
                paused=not paused

            if event.key==pygame.K_LEFT and direction!="RIGHT":
                direction="LEFT"
            if event.key==pygame.K_RIGHT and direction!="LEFT":
                direction="RIGHT"
            if event.key==pygame.K_UP and direction!="DOWN":
                direction="UP"
            if event.key==pygame.K_DOWN and direction!="UP":
                direction="DOWN"

    if paused:
        draw_text("PAUSED",250,180)
        pygame.display.update()
        continue

    move_snake()

    if collision():
        game_over()

    screen.fill(BLACK)

    for block in snake:
        pygame.draw.rect(screen,GREEN,(*block,BLOCK,BLOCK))

    pygame.draw.rect(screen,RED,(*food,BLOCK,BLOCK))

    draw_text(f"Score: {score}",10,10)

    pygame.display.update()
    clock.tick(speed)