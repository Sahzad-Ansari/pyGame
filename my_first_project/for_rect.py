import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = 900, 500

SCREEN = pygame.display.set_mode(SIZE)
WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

rect_x = 0
rect_y = 0
rect_w = 50
rect_h = 50
move_x = 0
move_y = 0

while True:
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 0.5
            elif event.key == pygame.K_LEFT:
                move_x = -0.5
        else:
            move_x = 0

    SCREEN.fill(WHITE)

    # surface,color,[x,y,w,h]
    pygame.draw.rect(SCREEN, RED, [rect_x, rect_y, rect_w, rect_h])
    rect_x += move_x

    # update the screen
    pygame.display.flip()
