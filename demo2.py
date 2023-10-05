import pygame
import random
import sys


# Initialize pygame
pygame.init()

# Set the dimensions of the window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# Create the window and set its title
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Moving rectangle")

# Set the dimensions of the rectangle
RECT_WIDTH = 30
RECT_HEIGHT = 20

# Set the initial position of the rectangle
rect_x = WINDOW_WIDTH // 2 - RECT_WIDTH // 2
rect_y = WINDOW_HEIGHT - RECT_HEIGHT - 10

# Set the velocity of the rectangle
VEL = 10

# Set the dimensions of the hole
hole_x = -1
hole_y = -1
HOLE_WIDTH = 50
HOLE_HEIGHT = 45

# Set the interval for generating a new hole
SPAWN_INTERVAL = 300 # 5 seconds in milliseconds

# Set the initial time for generating a new hole
current_time = pygame.time.get_ticks()

# Set the initial position of the line
LINE_START = (0, WINDOW_HEIGHT // 2)
LINE_END = (WINDOW_WIDTH, WINDOW_HEIGHT // 2)

# palyers
player1_x = WINDOW_WIDTH // 2 - RECT_WIDTH // 2
player1_y = WINDOW_HEIGHT - RECT_HEIGHT - 10
player2_x = WINDOW_WIDTH // 2 - RECT_WIDTH // 2
player2_y = 10

#counter
counter = 0
font = pygame.font.SysFont('Arial', 30)
#python

# Main loop
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rect_x > 0:
        rect_x -= VEL
    if keys[pygame.K_RIGHT] and rect_x < WINDOW_WIDTH - RECT_WIDTH:
        rect_x += VEL
    if keys[pygame.K_UP] and rect_y > 0:
        rect_y -= VEL
    if keys[pygame.K_DOWN] and rect_y < WINDOW_HEIGHT - RECT_HEIGHT:
        rect_y += VEL
    keys2 = pygame.key.get_pressed()
    if keys2[pygame.K_a] and rect2_x > 0:
        rect2_x -= VEL
    if keys2[pygame.K_d] and rect2_x < WINDOW_WIDTH - RECT_WIDTH:
        rect2_x += VEL
    if keys2[pygame.K_w] and rect2_y > 0:
        rect2_y -= VEL
    if keys2[pygame.K_s] and rect2_y < WINDOW_HEIGHT - RECT_HEIGHT:
        rect2_y += VEL

    # Update the position of the line
    LINE_START = (LINE_START[0] + 1, LINE_START[1])
    LINE_END = (LINE_END[0] + 1, LINE_END[1])

    # Check if it's time to generate a new hole
    if pygame.time.get_ticks() - current_time >= SPAWN_INTERVAL:
        hole_x = random.randint(0, WINDOW_WIDTH - HOLE_WIDTH)
        hole_y = random.randint(0, WINDOW_HEIGHT - HOLE_HEIGHT)
        current_time += pygame.time.get_ticks()



    # Fill the window with white
    win.fill((0, 0, 0))



    if pygame.Rect(rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT).colliderect(pygame.Rect(hole_x, hole_y, HOLE_WIDTH, HOLE_HEIGHT)):
        # The rectangle collided with the hole, destroy it
        hole_x = random.randint(0, WINDOW_WIDTH - HOLE_WIDTH)
        hole_y = random.randint(0, WINDOW_HEIGHT - HOLE_HEIGHT)
        HOLE_WIDTH -= 1

        current_time += pygame.time.get_ticks()
        run = False
        counter+=1


    pygame.draw.rect(win, (255, 0, 0), (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT))
    pygame.draw.rect(win, (0, 255, 0), (hole_x, hole_y, HOLE_WIDTH, HOLE_HEIGHT))

    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: {}".format(counter), True, (0, 0, 255))
    win.blit(score_text, (10, 10))


    # Draw the line
    pygame.draw.line(win, (0, 0, 255), LINE_START, LINE_END)

    # Update the display
    pygame.display.update()

    # Control the frame rate by delaying for a short time
    pygame.time.delay(10)
clock.tick(60)


# Quit pygame when the loop is exited
pygame.quit()
