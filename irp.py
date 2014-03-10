"""
The IRP Population Simulator
Written in Python
"""

"""
@author Andrew Li, Srishti Lulla, Akiva Gordon
"""
import pygame
import random
import sys
import time
pygame.init()

size = width, height = 500, 500
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
# counts number of neighbors to a cell


def find_neighbors(v, i, j):
    neighbor_count = 0
    for i_1 in range(3):
        for j_1 in range(3):
            """
            A lot of if's I know, but it's necessary.
            """
            if i - i_1 + 1 >= 0 and i - i_1 + 1 < len(v[0]):
                if j - j_1 + 1 >= 0 and j - j_1 + 1 < len(v[0]):
                    if v[i - i_1 + 1][j - j_1 + 1] == 1:
                        if i_1 != 1 or j_1 != 1:
                            neighbor_count += 1
    return neighbor_count

# updates the automata


def update_automata(v):  # assume v is a square array.
    length = len(v[0])
    v_final = [[0 for i in range(length)] for j in range(length)]
    buffer = 0
    for i in range(length):
        for j in range(length):
            buffer = find_neighbors(v, i, j)
            if v[i][j] == 1:
                if buffer < 2 or buffer > 3:
                    v_final[i][j] = 0
                else:
                    v_final[i][j] = 1
            elif v[i][j] == 0:
                if buffer == 3:
                    v_final[i][j] = 1
                else:
                    v_final[i][j] = 0
    return v_final
# This is for eating food
"""

            if v[i][j] == 1:
                if buffer < 2:
                    v_final[i][j] = 0
                elif buffer > 3:
                    v_final[i][j] = 0
                else:
                    v_final[i][j] = 1
            elif v[i][j] == 0:
                if buffer == 3:
                    v_final[i][j] = 1
                else:
                    v_final[i][j] = 0
            elif v[i][j] == 2:
                if buffer == 3:
                    v_final[i][j] = 0
                elif buffer == 2:
                    v_final[i][j] = 1
                else:
                    v_final[i][j] = 2
"""

# update_display() recalculates grid values


def update_display(length, values_grid, screen, box_size):
    for i in range(length):
        for j in range(length):
            if values_grid[i][j] == 1:  # 0 is white, 1 is black.
                pygame.draw.rect(
                    screen, black, pygame.Rect(
                        box_size*i, box_size*j, box_size,
                        box_size))
            elif values_grid[i][j] == 0:
                pygame.draw.rect(
                    screen, white, pygame.Rect(
                        box_size*i, box_size*j, box_size,
                        box_size))
            elif values_grid[i][j] == 2:
                pygame.draw.rect(
                    screen, red, pygame.Rect(
                        box_size*i, box_size*j, box_size,
                        box_size))
    pygame.display.flip()


def oscillator(length):
    grid = [
        [0 for i in range(length)] for j in range(length)
    ]
    grid[length / 2 - 1][length / 2] = 1
    grid[length / 2][length / 2] = 1
    grid[length / 2 + 1][length / 2] = 1
    return grid


def glider(length):
    grid = [
        [0 for i in range(length)] for j in range(length)
    ]
    grid[length / 2][length / 2 + 1] = 1
    grid[length / 2][length / 2] = 1
    grid[length / 2][length / 2 - 1] = 1
    grid[length / 2 - 1][length / 2 + 1] = 1
    grid[length / 2 - 2][length / 2] = 1
    return grid


def diamond_growth(length):
    grid = [
        [0 for i in range(length)] for j in range(length)
    ]
    grid[length / 2][length / 2] = 1
    grid[length / 2 + 2][length / 2] = 1
    grid[length / 2 + 1][length / 2 - 1] = 1
    grid[length / 2 + 1][length / 2 + 1] = 1
    grid[length / 2 + 1][length / 2] = 1
    return grid


def big_diamond_growth(length):
    grid = [
        [0 for i in range(length)] for j in range(length)
    ]
    grid[length / 2][length / 2] = 1
    grid[length / 2][length / 2 - 1] = 1
    grid[length / 2][length / 2 + 1] = 1
    grid[length / 2][length / 2 + 2] = 1
    grid[length / 2][length / 2 - 2] = 1
    grid[length / 2 + 1][length / 2] = 1
    grid[length / 2 + 1][length / 2 - 1] = 1
    grid[length / 2 + 1][length / 2 + 1] = 1
    grid[length / 2 - 1][length / 2] = 1
    grid[length / 2 - 1][length / 2 - 1] = 1
    grid[length / 2 - 1][length / 2 + 1] = 1
    grid[length / 2 + 2][length / 2] = 1
    grid[length / 2 - 2][length / 2] = 1
    return grid


def dual_pulsar(length):
    grid = [
        [0 for i in range(length)] for j in range(length)
    ]
    i = 0
    while i <= 4:
        grid[length / 2][length / 2 + i] = 1
        grid[length / 2][length / 2 - 1 + i] = 1
        grid[length / 2][length / 2 - 2 + i] = 1
        grid[length / 2][length / 2 + 4 + i] = 1
        grid[length / 2][length / 2 + 5 + i] = 1
        grid[length / 2][length / 2 + 6 + i] = 1
        grid[length / 2 - 5][length / 2 + i] = 1
        grid[length / 2 - 5][length / 2 - 1 + i] = 1
        grid[length / 2 - 5][length / 2 - 2 + i] = 1
        grid[length / 2 - 5][length / 2 + 4 + i] = 1
        grid[length / 2 - 5][length / 2 + 5 + i] = 1
        grid[length / 2 - 5][length / 2 + 6 + i] = 1
        grid[length / 2 + 2][length / 2 + i] = 1
        grid[length / 2 + 2][length / 2 - 1 + i] = 1
        grid[length / 2 + 2][length / 2 - 2 + i] = 1
        grid[length / 2 + 2][length / 2 + 4 + i] = 1
        grid[length / 2 + 2][length / 2 + 5 + i] = 1
        grid[length / 2 + 2][length / 2 + 6 + i] = 1
        grid[length / 2 + 7][length / 2 + i] = 1
        grid[length / 2 + 7][length / 2 - 1 + i] = 1
        grid[length / 2 + 7][length / 2 - 2 + i] = 1
        grid[length / 2 + 7][length / 2 + 4 + i] = 1
        grid[length / 2 + 7][length / 2 + 5 + i] = 1
        grid[length / 2 + 7][length / 2 + 6 + i] = 1
        i += 4
    return grid
"""
    grid[length / 2 + 1][length / 2] = 1
    grid[length / 2 + 1][length / 2 - 1] = 1
    grid[length / 2 + 1][length / 2 + 1] = 1
    grid[length / 2 - 1][length / 2] = 1
    grid[length / 2 - 1][length / 2 - 1] = 1
    grid[length / 2 - 1][length / 2 + 1] = 1
    grid[length / 2 + 2][length / 2] = 1
    grid[length / 2 - 2][length / 2] = 1
"""


def conway():
    box_size = raw_input(
        "Please enter the size at which you wish the boxes to display: ")
    box_size = int(box_size)
    length = raw_input(
        "Please enter the size of the cellular automata (<250): ")
    length = int(length)
    size = box_size*length, box_size*length  # used for creating screen
    values_grid = [
        [0 for i in range(length)] for j in range(length)
    ]  # stores values
    screen = pygame.display.set_mode(size)

    # initialize array
    for i in range(length):
        for j in range(length):
            values_grid[i][j] = random.randint(0, 1)

    """
    Uncomment one of these to choose a pre-set pattern.
    """
    # values_grid = oscillator(length)
    # values_grid = glider(length)
    # values_grid = diamond_growth(length)
    # values_grid = big_diamond_growth(length)
    values_grid = dual_pulsar(length)
    while True:
        update_display(length, values_grid, screen, box_size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # this function is shown above.
        values_grid = update_automata(values_grid)
        time.sleep(0.5)

conway()
