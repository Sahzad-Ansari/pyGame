import pygame
import  random
pygame.init()

SIZE = WIDTH, HEIGHT = 1500, 700
SCREEN = pygame.display.set_mode(SIZE)

BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
BLUE = 0,0,255

SPEED = 1
rect_x = 0
rect_y = 0
move_x = SPEED
move_y = SPEED
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   # will quit pygame
            quit()  # will quit python

    SCREEN.fill(WHITE)
    color = random.randint(0,255), random.randint(0,255), random.randint(0,255)
    pygame.draw.rect(SCREEN, color, [rect_x, rect_y, 100, 100])
    rect_x += move_x
    rect_y += move_y

    if rect_x > WIDTH - 100:
        move_x = -SPEED
    elif rect_x < 0:
        move_x = SPEED

    if rect_y > HEIGHT - 100:
        move_y = -SPEED
    elif rect_y < 0:
        move_y = SPEED

    pygame.display.flip()