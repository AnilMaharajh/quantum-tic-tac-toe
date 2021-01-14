import pygame
# import pygame_gui
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
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
# 0 is omitted since it already corresponds to the first position on the game board
INDEX_TO_BOARD_POSITION = {}


def place_marker(x, y, game: TicTacToe):
    """Given x, y coordinates, the player character and the subscript, places
    the marker on the quantum board"""
    print(x, y, len(KEY_COOR_SMALL))
    for index in range(len(KEY_COOR_SMALL)):
        bool1 = KEY_COOR_SMALL[index][0] <= x < KEY_COOR_SMALL[index][2] + KEY_COOR_SMALL[index][0]
        bool2 = KEY_COOR_SMALL[index][1] <= y < KEY_COOR_SMALL[index][3] + KEY_COOR_SMALL[index][1]
        if bool1 and bool2:
            print(x, y)
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
                # entangle = game.entangle()
                # if entangle != []:
                #     game.collapse(entangle)


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


def entangle_move(x, y, char: str):
    """Clears a section of the grid and replaces it with char"""
    for index in range(len(KEY_COOR)):
        bool1 = KEY_COOR[index][0] <= x < KEY_COOR[index][2] + KEY_COOR[index][0]
        bool2 = KEY_COOR[index][1] <= y < KEY_COOR[index][3] + KEY_COOR[index][1]
        if bool1 and bool2 and char.lower() == "x":
            pygame.draw.rect(
                window_surface,
                WHITE,
                KEY_COOR[index]
            )
            font1 = pygame.font.Font('freesansbold.ttf', 120)
            text1 = font1.render('X', True, BLACK, WHITE)
            text_rect = text1.get_rect()
            text_rect.center = (
                KEY_COOR[index][0] + KEY_COOR[index][2] / 2,
                KEY_COOR[index][1] + KEY_COOR[index][3] / 2
            )
            window_surface.blit(text1, text_rect)
        elif bool1 and bool2 and char.lower() == "o":
            pygame.draw.rect(
                window_surface,
                WHITE,
                KEY_COOR[index]
            )
            font1 = pygame.font.Font('freesansbold.ttf', 120)
            text1 = font1.render('O', True, BLACK, WHITE)
            text_rect = text1.get_rect()
            text_rect.center = (
                KEY_COOR[index][0] + KEY_COOR[index][2] / 2,
                KEY_COOR[index][1] + KEY_COOR[index][3] / 2
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

font = pygame.font.Font('freesansbold.ttf', 21)
text = font.render('DO YOU WANT TO PLAY A BETTER TIC-TAC-TOE? CLICK ANYWHERE IF YES', True, GREEN, RED)

window_surface.fill(WHITE)

# manager = pygame_gui.UIManager((800, 600))

# hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
#                                             text='Say Hello',
#                                             manager=manager)
# clock = pygame.time.Clock()
is_running = True
start = False
entangle = False
game = TicTacToe()

while is_running:
    if not start:
        window_surface.blit(text, text.get_rect())
    if start:
        window_surface.blit(image, (0, 0))
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
                place_marker(event.pos[0], event.pos[1], game)
                entangler = game.entangle()
                if entangler:
                    game.collapse(entangler)
                    entangle = not not entangler

            elif start and entangle:
                # Right now the third parameter is "O", but it can be whatever
                # you like later
                entangle_move(event.pos[0], event.pos[1], "O")

        # if event.type == pygame.USEREVENT:
        #     if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
        #         if event.ui_element == hello_button:
        #             print('Hello World!')

    #     manager.process_events(event)
    #
    # manager.update(time_delta)

    # window_surface.blit(background, (0, 0))
    # manager.draw_ui(window_surface)

    pygame.display.update()
