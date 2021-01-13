import pygame
# import pygame_gui
import tictactoe

FONT_SIZE = 30
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def create_grid():
    window_surface.fill(WHITE)
    for i in range(9):
        if i % 3 == 0:
            pygame.draw.line(
                window_surface,
                BLACK,
                (i * WIDTH/9, 0.0),
                (i * WIDTH/9, HEIGHT),
                5
            )
            pygame.draw.line(
                window_surface,
                BLACK,
                (0.0, i * HEIGHT/9),
                (WIDTH, i * HEIGHT/9),
                5
            )
        else:
            pygame.draw.line(
                window_surface,
                BLACK,
                (i * WIDTH/9, 0.0),
                (i * WIDTH/9, HEIGHT),
                3
            )
            pygame.draw.line(
                window_surface,
                BLACK,
                (0.0, i * HEIGHT/9),
                (WIDTH, i * HEIGHT/9),
                3
            )


pygame.init()

pygame.display.set_caption('Quantum Tic-Tac-Toe')
window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font('freesansbold.ttf', 21)
text = font.render('DO YOU WANT TO PLAY A BETTER TIC-TAC-TOE? CLICK ANYWHERE IF YES', True, GREEN, RED)

window_surface.fill(WHITE)

# manager = pygame_gui.UIManager((800, 600))

# hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
#                                             text='Say Hello',
#                                             manager=manager)
# game = tictactoe.TicTacToe()
# clock = pygame.time.Clock()
is_running = True
start = False

while is_running:
    if not start:
        window_surface.blit(text, text.get_rect())
    # time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.MOUSEBUTTONUP:
            if not start:
                start = True
                create_grid()
            else:
                pass

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
