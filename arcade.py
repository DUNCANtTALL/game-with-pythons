import pygame
import sys
from pygame.locals import *


pygame.init()

# screen
width = 8
height = 8
tilesize = 30
win = pygame.display.set_mode((width*55, height*55))
pygame.display.set_caption("arcade")

# map
mat = {
    "wall": 0,
    "floor": 1,
    "plant": 2
}

# colors
colors = {
    "wall": (255, 255, 255),
    "plant": (0, 255, 0),
    "player": (255, 0, 0)
}

# tilemap
tilemap = [     [mat["wall"], mat["wall"], mat["floor"], mat["wall"], mat["wall"], mat["wall"], mat["wall"]],
    [mat["wall"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["wall"]],
    [mat["wall"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["wall"]],
    [mat["wall"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["wall"]],
    [mat["wall"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["wall"]],
    [mat["wall"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["wall"]],
    [mat["wall"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["floor"], mat["wall"]],
    [mat["wall"], mat["wall"], mat["wall"], mat["wall"], mat["wall"], mat["wall"], mat["wall"], mat["wall"]]
]

# player
player_pos = [1, 1]

# game loop
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                loop = False

            # move player
            if event.key == K_UP and tilemap[player_pos[1]-1][player_pos[0]] != mat["wall"]:
                player_pos[1] -= 1
            elif event.key == K_DOWN and tilemap[player_pos[1]+1][player_pos[0]] != mat["wall"]:
                player_pos[1] += 1
            elif event.key == K_LEFT and tilemap[player_pos[1]][player_pos[0]-1] != mat["wall"]:
                player_pos[0] -= 1
            elif event.key == K_RIGHT and tilemap[player_pos[1]][player_pos[0]+1] != mat["wall"]:
                player_pos[0] += 1

    # draw tilemap
    for row in range(height):
        for col in range(width - 1):
            tile = tilemap[row][col]
            color = colors["wall"] if tile == mat["wall"] else colors["plant"]
            pygame.draw.rect(win, color, (col * tilesize, row * tilesize, tilesize, tilesize))

        # draw player
        pygame.draw.rect(win, colors["player"],(player_pos[0] * tilesize, player_pos[1] * tilesize, tilesize, tilesize))
        pygame.display.update()
    pygame.quit()
    sys.exit()