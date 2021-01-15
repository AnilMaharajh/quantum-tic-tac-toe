import pygame
from tictactoe import TicTacToe

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
# 0 is omitted since it already corresponds to the first position on the game board
INDEX_TO_BOARD_POSITION = {}
VALID_MOVES = {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True}
# Allows variables to be mutated in functions
CHOSEN_BOX = []
COLLAPSE_MARK1 = []
COLLAPSE_MARK2 = []
# pygame grid number goes down instead of across like in tictactoe.py
CONVERT_POS = {0: 0, 1: 3, 2: 6, 3: 1, 4: 4, 5: 7, 6: 2, 7: 5, 8: 8}


def place_marker(x, y, game: TicTacToe):
    """Given x, y coordinates, the player character and the subscript, places
    the marker on the quantum board"""
    for index in range(len(KEY_COOR_SMALL)):
        bool1 = KEY_COOR_SMALL[index][0] <= x < KEY_COOR_SMALL[index][2] + KEY_COOR_SMALL[index][0]
        bool2 = KEY_COOR_SMALL[index][1] <= y < KEY_COOR_SMALL[index][3] + KEY_COOR_SMALL[index][1]
        if bool1 and bool2:
            # Can replace the mark on the board, but game.board will not be overidden
            position = get_position(x, y)
            mark = game.place_piece(position)
            if mark != "F":
                print(mark)
                font1 = pygame.font.Font('freesansbold.ttf', 32)
                text1 = font1.render(f'{mark}', True, BLACK, WHITE)
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

    CONVERT_POS = {0: 0, 1: 3, 2: 6, 3: 1, 4: 4, 5: 7, 6: 2, 7: 5, 8: 8}
    # Changes all the valid moves to False
    for key in VALID_MOVES.keys():
        VALID_MOVES[key] = False
    print(entangle)
    for box in entangle:
        VALID_MOVES[box] = True
        pygame.draw.rect(
            window_surface,
            BLUE,
            KEY_COOR[CONVERT_POS[box]], 3
        )


def get_position(x: int, y: int):
    """
    Takes in the x and y coordinate where the user clicked, and
    returns the position where the click corresponds to the board
    :return: an integer from 0-8 corresponding to a board position
    """
    print(x, y)
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
    elif 500 <= x <= 725 and 730 <= y <= 955:
        return COLLAPSE_MARK1[0]
    elif 825 <= x <= 855 and 730 <= y <= 955:
        return COLLAPSE_MARK2[0]
    else:
        return 9


def entangle_move(x, y):
    """If a player clicks on a valid square, 2 marks will be
    displayed for the user to choose for a collapse
    """
    index = get_position(x, y)
    if VALID_MOVES[index]:
        COLLAPSE_MARK1.append(game.board[index][0])
        COLLAPSE_MARK2.append(game.board[index][-1])
        CHOSEN_BOX.append(index)
    else:
        print("Invalid move")


def collapse(box, mark):
    """
    Changes the boxes in grid into classical moves
    :param box:
    :return:
    """
    coll = game.collapse(box, mark)
    coll[box] = mark
    print(coll)
    for key, value in coll.items():
        if VALID_MOVES[key]:
            game.place_classical(coll)
            pygame.draw.rect(
                window_surface,
                BLACK,
                KEY_COOR[CONVERT_POS[key]]
            )
            font1 = pygame.font.Font('freesansbold.ttf', 120)
            text1 = font1.render(f"{value}", True, BLACK, WHITE)
            text_rect = text1.get_rect()
            text_rect.center = (
                KEY_COOR[CONVERT_POS[key]][0] + KEY_COOR[CONVERT_POS[key]][2] / 2,
                KEY_COOR[CONVERT_POS[key]][1] + KEY_COOR[CONVERT_POS[key]][3] / 2
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


def choices():
    """Puts up the choices of which token should be on the board"""
    font_choice_1 = pygame.font.Font('freesansbold.ttf', 40)
    font_choice_2 = pygame.font.Font('freesansbold.ttf', 40)

    text_choice_1 = font_choice_1.render(f"{COLLAPSE_MARK1[0]}", True, BLACK, RED)
    text_choice_2 = font_choice_2.render(f"{COLLAPSE_MARK2[0]}", True, WHITE, BLUE)

    text_choice_1_rect = text_choice_1.get_rect()
    text_choice_2_rect = text_choice_2.get_rect()

    text_choice_1_rect.center = (225 + 300, 100 + 603 + 40)
    text_choice_2_rect.center = (225 + 600, 100 + 603 + 40)

    window_surface.blit(text_choice_1, text_choice_1_rect)
    window_surface.blit(text_choice_2, text_choice_2_rect)


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
colpse = False
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
            x = event.pos[0]
            y = event.pos[1]
            position = get_position(x, y)
            if not start:
                start = True
                create_grid()

            elif start and not entangle:
                entangle = place_marker(x, y, game)
                print(entangle)

            elif start and entangle and type(position) == int:
                print("entangle happens")
                entangle_move(event.pos[0], event.pos[1])
                choices()
                colpse = True

            elif start and colpse and type(position) == str:
                print("ay o collapse")
                collapse(CHOSEN_BOX[0], position)
                winners = game.check_winner()
                if winners["X"] > 0 or winners["O"] > 0:
                    print("Winner")
                    break
                entangle = False
                colpse = False
                CHOSEN_BOX.pop()
                COLLAPSE_MARK1.pop()
                COLLAPSE_MARK2.pop()
                for i in range(len(game.board)):
                    # If a box was entangled return it back to Black
                    if VALID_MOVES[i]:
                        pygame.draw.rect(
                            window_surface,
                            BLACK,
                            KEY_COOR[CONVERT_POS[i]], 3
                        )
                    if type(game.board[i]) == str:
                        VALID_MOVES[i] = False
                    else:
                        VALID_MOVES[i] = True
                print(VALID_MOVES)

    pygame.display.update()
