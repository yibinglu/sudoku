# gui.py
# Pygame UI

from multiprocessing.util import close_all_fds_except
from pprint import pprint
from select import select
import pygame
import time
from logic import solve_grid, check_num
import copy
import math
from pygame.locals import *

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

cell_x = 0
cell_y = 0

add_num = False
highlight_num = False
select_num = ''

# possibilities = []
# for i in range(rows):
#     possibilities.append([])
#     for j in range(cols):
#         possibilities[i].append([])


def draw_outline(window):
    for i in range(rows+1):
        if i % 3 == 0 and i != 0:
            weight = 4

        else:
            weight = 1

        pygame.draw.line(window, (0, 0, 0), (0, i*cell_width),
                         (win_width, i*cell_width), weight)
        pygame.draw.line(window, (0, 0, 0), (i * cell_width, 0),
                         (i * cell_width, board_height), weight)


def draw_grid(window):
    for y in range(rows):
        for x in range(cols):
            print(add_num, cell_x, cell_y, x, y)
            if (add_num and x == cell_x and y == cell_y) or (highlight_num and int(player_board[y][x]) == select_num):
                print('highlight')
                rect = Rect(50, 60, cell_width, cell_height)
                pygame.draw.rect(window, (211, 211, 211), rect)

            if player_board[y][x] != 0:
                fnt = pygame.font.SysFont("timesnewroman", 40)
                text = fnt.render(str(player_board[y][x]), 1, (0, 0, 0))
                window.blit(text, (cell_width/3 + x*cell_width,
                            cell_height/6 + y*cell_height))
                # possibilities[y][x] = []

    draw_outline(window)


def mouse_pressed():
    highlight_num = False
    add_num = False
    mouse_x, mouse_y = pygame.mouse.get_pos()
    x = math.floor(mouse_x/cell_width)
    y = math.floor(mouse_y/cell_height)

    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        if int(player_board[y][x]) != 0:
            highlight_num = True

            if BOARD[y][x] != 0:
                select_num = BOARD[y][x]

            else:
                select_num = int(player_board[y][x])

        if BOARD[y][x] == 0:
            add_num = True
            cell_x = x
            cell_y = y
            print(add_num, cell_x, cell_y, x, y)


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

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed()

            draw_window(window)

    pygame.quit()


main()
