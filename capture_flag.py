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
player1_score = 0
player2_score = 0
font = pygame.font.SysFont('Arial', 30)


# Main loop
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle keyboard input
    # Player 1 controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player1_x > 0:
        player1_x -= VEL
    if keys[pygame.K_RIGHT] and player1_x < WINDOW_WIDTH - RECT_WIDTH:
        player1_x += VEL
    if keys[pygame.K_UP] and player1_y > 0:
        player1_y -= VEL
    if keys[pygame.K_DOWN] and player1_y < WINDOW_HEIGHT - RECT_HEIGHT:
        player1_y += VEL

    # Player 2 controls
    if keys[pygame.K_a] and player2_x > 0:
        player2_x -= VEL
    if keys[pygame.K_d] and player2_x < WINDOW_WIDTH - RECT_WIDTH:
        player2_x += VEL
    if keys[pygame.K_w] and player2_y > 0:
        player2_y -= VEL
    if keys[pygame.K_s] and player2_y < WINDOW_HEIGHT - RECT_HEIGHT:
        player2_y += VEL
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

    if pygame.Rect(player1_x, player1_y, RECT_WIDTH, RECT_HEIGHT).colliderect(
            pygame.Rect(hole_x, hole_y, HOLE_WIDTH, HOLE_HEIGHT)):
        # Player 1 collided with the hole, increase their score
        hole_x = random.randint(0, WINDOW_WIDTH - HOLE_WIDTH)
        hole_y = random.randint(0, WINDOW_HEIGHT - HOLE_HEIGHT)
        HOLE_WIDTH -= 1
        RECT_WIDTH += 5
        current_time += pygame.time.get_ticks()
        player1_score += 1

    if pygame.Rect(player2_x, player2_y, RECT_WIDTH, RECT_HEIGHT).colliderect(
            pygame.Rect(hole_x, hole_y, HOLE_WIDTH, HOLE_HEIGHT)):
        # Player 2 collided with the hole, increase their score
        hole_x = random.randint(0, WINDOW_WIDTH - HOLE_WIDTH)
        hole_y = random.randint(0, WINDOW_WIDTH - HOLE_WIDTH)
        HOLE_WIDTH -= 1

        current_time += pygame.time.get_ticks()
        player2_score += 1




    pygame.draw.rect(win, (255, 0, 0), (player1_x, player1_y, RECT_WIDTH, RECT_HEIGHT))
    pygame.draw.rect(win, (0, 0, 255), (player2_x, player2_y, RECT_WIDTH, RECT_HEIGHT))
    pygame.draw.rect(win, (0, 255, 0), (hole_x, hole_y, HOLE_WIDTH, HOLE_HEIGHT))


    font = pygame.font.Font(None, 36)
    score_text = font.render("Score 1: {}".format(player1_score), True, (170, 51,106 ))
    win.blit(score_text, (10, 10))
    score_text = font.render("Score 2: {}".format(player2_score), True, (0, 0, 255))
    win.blit(score_text, (10, 50))

    # Update the display
    pygame.display.update()

    # Control the frame rate by delaying for a short time
    pygame.time.delay(10)
clock.tick(60)


# Quit pygame when the loop is exited
pygame.quit()
