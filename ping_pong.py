import pygame
import random
import sys

pygame.init()

# Set the dimensions of the window
win_width = 800
win_height = 500

# Create the window and set its title
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("ping pong")

# Define the playable object dimensions and velocity
paddle_width = 7
paddle_height = 100
paddle_velocity = 10

# Define the ball dimensions, color, position, and velocity
ball_radius = 20
ball_color = (255, 255, 255)
ball_pos = [250, 255]
ball_speed = [2, 2]

# Define the players' initial positions
player1_x = 50
player1_y = 200
player2_x =740
player2_y = 200
# score
score1 =0
score2 =0
font = pygame.font.SysFont('Arial', 30)


# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle keyboard input
        # Player 1 controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_velocity -3
    if keys[pygame.K_DOWN] and player2_y < win_height - paddle_height:
        player2_y += paddle_velocity -3

    # Player 2 controls
    if keys[pygame.K_z] and player1_y > 0:
        player1_y -= paddle_velocity -3
    if keys[pygame.K_s] and player1_y < win_height - paddle_height:
        player1_y += paddle_velocity -3


    # Update the ball position
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Bounce the ball off the walls
    if ball_pos[0] < ball_radius or ball_pos[0] > win_width - ball_radius:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= ball_radius or ball_pos[1] >= win_height - ball_radius:
        ball_speed[1] = -ball_speed[1]
        # Check for collision with the paddles
    if pygame.Rect(player1_x, player1_y, paddle_width, paddle_height).colliderect(
            (ball_pos[0] - ball_radius, ball_pos[1] - ball_radius, ball_radius * 2, ball_radius * 2)):
        ball_speed[0] = abs(ball_speed[0])  # Make the ball bounce instantly when hitting the paddles
    if pygame.Rect(player2_x, player2_y, paddle_width, paddle_height).colliderect(
            (ball_pos[0] - ball_radius, ball_pos[1] - ball_radius, ball_radius * 2, ball_radius * 2)):
        ball_speed[0] = -abs(ball_speed[0])  # Make the ball bounce instantly when hitting the paddles

    if ball_pos[0] >= win_width - ball_radius:
        score1+=1
    if ball_pos[0] <=  ball_radius:
        score2+=1




    # Draw the objects
    win.fill((0, 0, 0))
    pygame.draw.circle(win, ball_color, ball_pos, ball_radius)
    pygame.draw.rect(win, (255, 255, 255), (player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(win, (255, 255, 255), (player2_x, player2_y, paddle_width, paddle_height))
    pygame.time.delay(3)
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score 1: {}".format(score1), True, (170, 51, 106))
    win.blit(score_text, (10, 10))
    score_text = font.render("Score 2: {}".format(score2), True, (0, 0, 255))
    win.blit(score_text, (10, 50))

    # Update the display
    pygame.display.update()
