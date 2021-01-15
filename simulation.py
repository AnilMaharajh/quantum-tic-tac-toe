import pygame
# import pygame_gui
from tictactoe import TicTacToe
from tkinter import *
from tkinter import messagebox

FONT_SIZE = 30
WIDTH = 1350
HEIGHT = 800
GAME_WIDTH = WIDTH * 2 // 3
GAME_HEIGHT = HEIGHT * 3 // 4 + 3
KEY_COOR = []
for i in range(225, 1125, 300):
    for j in range(100, 703, 201):
        KEY_COOR.append((i + 2.5, j + 2.5, 297.5, 198.5))

KEY_COOR_SMALL = []
for i in range(225, 1125, 100):
    for j in range(100, 703, 67):
        KEY_COOR_SMALL.append((i + 2.5, j + 2.5, 97.5, 64.5))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
# 0 is omitted since it already corresponds to the first position on the game board
INDEX_TO_BOARD_POSITION = {}
VALID_MOVES = {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True}
COLLAPSE_MARK1 = []
COLLAPSE_MARK2 = []


def place_marker(x, y, game: TicTacToe):
    """Given x, y coordinates, the player character and the subscript, places
    the marker on the quantum board"""
    print(x, y)
    for index in range(len(KEY_COOR_SMALL)):
        bool1 = KEY_COOR_SMALL[index][0] <= x < KEY_COOR_SMALL[index][2] + KEY_COOR_SMALL[index][0]
        bool2 = KEY_COOR_SMALL[index][1] <= y < KEY_COOR_SMALL[index][3] + KEY_COOR_SMALL[index][1]
        if bool1 and bool2:
            # Can replace the mark on the board, but game.board will not be overidden
            position = get_position(x, y)
            mark = game.place_piece(position)
            if mark != "F":
                font1 = pygame.font.Font('freesansbold.ttf', 32)
                text1 = font1.render(f'{mark[0]}{mark[1]}'.translate(SUB), True, BLACK, WHITE)
                text_rect = text1.get_rect()
                text_rect.center = (
                    KEY_COOR_SMALL[index][0] + KEY_COOR_SMALL[index][2] / 2,
                    KEY_COOR_SMALL[index][1] + KEY_COOR_SMALL[index][3] / 2
                )
                window_surface.blit(text1, text_rect)
                entangle_check = game.entangle()
                if entangle_check:
                    # Create an outline around the entangled boxes
                    entangled_boxes(entangle_check)
                    return True
    return False


def entangled_boxes(entangle):
    """
    Puts a blue outline around boxes that can collapse
    :param entangle: A list that contains all the positions that are entangled
    """
    # pygame grid number goes down instead of across like in tictactoe.py
    convert_pos = {0: 0, 1: 3, 2: 6, 3: 2, 4: 4, 5: 7, 6: 7, 7: 5, 8: 8}
    # Changes all the valid moves to False
    for key in VALID_MOVES.keys():
        VALID_MOVES[key] = False
    for box in entangle:
        VALID_MOVES[box] = True
        pygame.draw.rect(
            window_surface,
            BLUE,
            KEY_COOR[convert_pos[box]], 3
        )


def get_position(x: int, y: int):
    """
    Takes in the x and y coordinate where the user clicked, and
    returns the position where the click corresponds to the board
    :return: an integer from 0-8 corresponding to a board position
    """
    if 255 < x < 525 and 100 < y < 300:
        return 0
    elif 255 < x < 525 and 300 < y < 500:
        return 3
    elif 255 < x < 525 and 500 < y < 700:
        return 6
    elif 525 < x < 795 and 100 < y < 300:
        return 1
    elif 525 < x < 795 and 300 < y < 500:
        return 4
    elif 525 < x < 795 and 500 < y < 700:
        return 7
    elif 795 < x < 1120 and 100 < y < 300:
        return 2
    elif 795 < x < 1120 and 300 < y < 500:
        return 5
    elif 795 < x < 1120 and 500 < y < 700:
        return 8
    else:
        return 9


def entangle_move(x, y):
    """If a player clicks on a valid square, 2  marks will be
    displayed for the user to choose for a collapse
    """
    index = get_position(x, y)
    print(index)
    if VALID_MOVES[index]:
        collapse_box = game.collapse(index, game.board[index][0])
        print(collapse_box)
        game.place_classical(collapse_box)
        COLLAPSE_MARK1.append(collapse_box[0])
        COLLAPSE_MARK2.append(collapse_box[0])

        pygame.draw.rect(window_surface, BLACK, (360, 722))
        font1 = pygame.font.Font('freesansbold.ttf', 120)
        text1 = font1.render(COLLAPSE_MARK1[0], True, BLACK, WHITE)
        text_rect = text1.get_rect()
        window_surface.blit(text1, text_rect)

        pygame.draw.rect(window_surface, BLACK, (500, 722))
        font1 = pygame.font.Font('freesansbold.ttf', 120)
        text1 = font1.render(COLLAPSE_MARK2[0], True, BLACK, WHITE)
        text_rect = text1.get_rect()
        window_surface.blit(text1, text_rect)
        print(game.board)
    else:
        print("Invalid move")


def collapse(box, mark):
    """
    Changes the boxes in grid into classical moves
    :param box:
    :return:
    """
    for key, value in game.collapse(box, mark):
        if VALID_MOVES[key]:
            pygame.draw.rect(
                window_surface,
                BLACK,
                KEY_COOR[key]
            )
            font1 = pygame.font.Font('freesansbold.ttf', 120)
            text1 = font1.render(value, True, BLACK, WHITE)
            text_rect = text1.get_rect()
            text_rect.center = (
                KEY_COOR[key][0] + KEY_COOR[key][2] / 2,
                KEY_COOR[key][1] + KEY_COOR[key][3] / 2
            )
            window_surface.blit(text1, text_rect)


def create_grid():
    """Creates the grid for Tic-Tac-Toe"""
    window_surface.fill(WHITE)
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(
                window_surface,
                BLACK,
                (i * GAME_WIDTH / 9 + 225, 100.0),
                (i * GAME_WIDTH / 9 + 225, GAME_HEIGHT + 100),
                5
            )
            pygame.draw.line(
                window_surface,
                BLACK,
                (225.0, i * GAME_HEIGHT / 9 + 100),
                (225 + GAME_WIDTH, i * GAME_HEIGHT / 9 + 100),
                5
            )
        else:
            pygame.draw.line(
                window_surface,
                BLACK,
                (i * GAME_WIDTH / 9 + 225, 100.0),
                (i * GAME_WIDTH / 9 + 225, GAME_HEIGHT + 100),
                3
            )
            pygame.draw.line(
                window_surface,
                BLACK,
                (225.0, i * GAME_HEIGHT / 9 + 100),
                (225 + GAME_WIDTH, i * GAME_HEIGHT / 9 + 100),
                3
            )


pygame.init()

pygame.display.set_caption('Quantum Tic-Tac-Toe')
window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

image = pygame.image.load('player_image_1.jpeg')
image2 = pygame.image.load('image.jpg')

font = pygame.font.Font('freesansbold.ttf', 21)
text = font.render('DO YOU WANT TO PLAY A BETTER TIC-TAC-TOE? CLICK ANYWHERE IF YES', True, GREEN, RED)

font_title = pygame.font.Font('freesansbold.ttf', 40)
window_surface.fill(WHITE)

font_score = pygame.font.Font('freesansbold.ttf', 20)

is_running = True
start = False
entangle = False
game = TicTacToe()
score_p1 = 0
score_p2 = 0

while is_running:
    if not start:
        window_surface.blit(text, text.get_rect())
    if start:
        window_surface.blit(image, (0, 0))
        window_surface.blit(image2, (1145, 0))

        text_title = font_title.render("QUANTUM TIC-TAC-TOE", True, GREEN, WHITE)
        text_score_1 = font_score.render("X SCORE", True, RED, WHITE)
        text_score_2 = font_score.render("O SCORE", True, BLUE, WHITE)
        score_1 = font_score.render(f"{score_p1}", True, RED, WHITE)
        score_2 = font_score.render(f"{score_p2}", True, BLUE, WHITE)

        title_rect = text_title.get_rect()
        text_score_1_rect = text_score_1.get_rect()
        text_score_2_rect = text_score_2.get_rect()
        score_1_rect = score_1.get_rect()
        score_2_rect = score_2.get_rect()

        title_rect.center = (WIDTH / 2, 50)
        text_score_1_rect.center = (205 / 2, 246 + 30)
        text_score_2_rect.center = (WIDTH - 205 / 2, 246 + 30)
        score_1_rect.center = (205 / 2, 246 + 60)
        score_2_rect.center = (WIDTH - 205 / 2, 246 + 60)

        window_surface.blit(text_title, title_rect)
        window_surface.blit(text_score_1, text_score_1_rect)
        window_surface.blit(text_score_2, text_score_2_rect)
        window_surface.blit(score_1, score_1_rect)
        window_surface.blit(score_2, score_2_rect)

    # time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.MOUSEBUTTONUP:
            if not start:
                start = True
                create_grid()

            elif start and not entangle:
                # Right now the third parameter is "X", but it can be whatever
                # you like later, same with the fourth parameter
                entangle = place_marker(event.pos[0], event.pos[1], game)

            elif start and entangle:
                # Right now the third parameter is "O", but it can be whatever
                # you like later
                entangle_move(event.pos[0], event.pos[1])

    pygame.display.update()
