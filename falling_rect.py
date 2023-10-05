# import pygame module in this program
import pygame
import random
from pygame.locals import *

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension..e(500, 500).
win = pygame.display.set_mode((500, 500))

# set the pygame window name
pygame.display.set_caption("Moving rectangle")

# object current co-ordinates
x = 200
y = 200

# dimensions of the object
width = 20
height = 20

# velocity / speed of movement
vel = 10

# static object
wall_x = width/2
wall_y = height/2
wall_yc = 3 * random.choice((1, -1))
wall_xc = 3 * random.choice((1, -1))
wallp = 100

# object
player_rect = Rect(200, 500, 50, 50)
speed = 8
# Indicates pygame is running
run = True

# infinite loop
while run:
    # creates time delay of 10ms
    pygame.time.delay(10)
    player_rect.bottom += speed
    collide = pygame.Rect.colliderect(player_rect,(x, y, width, height))
    if collide:
        speed *= -1

    if player_rect.top < 0 or player_rect.bottom > 600:
        speed *= -1


    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # it will make exit the while loop
            run = False
    # stores keys pressed
    keys = pygame.key.get_pressed()

    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x > 0:
        # decrement in x co-ordinate
        x -= vel

    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x < 500 - width:
        # increment in x co-ordinate
        x += vel

    # if left arrow key is pressed
    if keys[pygame.K_UP] and y > 0:
        # decrement in y co-ordinate
        y -= vel

    # if left arrow key is pressed
    if keys[pygame.K_DOWN] and y < 500 - height:
        # increment in y co-ordinate
        y += vel

    # if the wall touches the win
        if wall_x + wallp >= 500 or wall_x <= 0 :
            wall_xc *= -1
        if wall_y + wallp >= 500 or wallp <= 0 :
            wall_yc *= -1
    # changes
    wall_y += wall_yc
    wall_x += wall_xc




    # completely fill the surface object
    # with black colour
    win.fill((0, 0, 0))

    # drawing object on screen which is rectangle here
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    ballImg = pygame.draw.circle(win, (255, 0,0),(int(wall_x), int(wall_y)),15)
    pygame.draw.rect(win, (0, 255, 0),player_rect)

    # it refreshes the window
    pygame.display.update()

# closes the pygame window
pygame.quit()
