# gui.py
# Pygame UI

from pprint import pprint
import pygame
import time
from logic import solve_grid, check_num
import copy

pygame.init()

BOARD = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
         [6, 8, 0, 0, 7, 0, 0, 9, 0],
         [1, 9, 0, 0, 0, 4, 5, 0, 0],
         [8, 2, 0, 1, 0, 0, 0, 4, 0],
         [0, 0, 4, 6, 0, 2, 9, 0, 0],
         [0, 5, 0, 0, 0, 3, 0, 2, 8],
         [0, 0, 9, 3, 0, 0, 0, 7, 4],
         [0, 4, 0, 0, 5, 0, 0, 3, 6],
         [7, 0, 3, 0, 1, 8, 0, 0, 0]]

player_board = copy.deepcopy(BOARD)
answer_board = copy.deepcopy(BOARD)

solve_grid(0, 0, answer_board)

rows = 9
cols = 9
win_width = 540
win_height = 600
board_height = 540
cell_width = win_width/cols
cell_height = board_height/rows

possibilities = []
for i in range(rows):
    possibilities.append([])
    for j in range(cols):
        possibilities[i].append([])


def draw_grid(window):
    for i in range(rows+1):
        if i % 3 == 0 and i != 0:
            weight = 4

        else:
            weight = 1

        pygame.draw.line(window, (0, 0, 0), (0, i*cell_width),
                         (win_width, i*cell_width), weight)
        pygame.draw.line(window, (0, 0, 0), (i * cell_width, 0),
                         (i * cell_width, board_height), weight)


def draw_window(window):
    window.fill((255, 255, 255))
    draw_grid(window)
    pygame.display.update()


def main():
    window = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(window)

    pygame.quit()


main()
