import pygame
pygame.init()
SIZE= WIDTH,HEIGHT=900,500

SCREEN=pygame.display.set_mode(SIZE)
WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255


circle_x=40
circle_y=40
radius=40
SPEED_X=0.4
SPEED_Y=0.4


while True:
     eventList = pygame.event.get()
     for event in eventList:
          if event.type == pygame.QUIT:
               pygame.quit()
               quit()

     SCREEN.fill(WHITE)

     pygame.draw.circle(SCREEN, BLUE, [circle_x, circle_y], radius)
     circle_x +=SPEED_X
     circle_y +=SPEED_Y

     circle_x += SPEED_X
     circle_y += SPEED_Y

     if circle_x > WIDTH - radius:
          SPEED_X = -0.4
     elif circle_y > HEIGHT - radius:
          SPEED_Y = -0.4
     elif circle_x <= radius:
          SPEED_X = 0.4
     elif circle_y <= radius:
          SPEED_Y = 0.4

          # update the screen
     pygame.display.flip()