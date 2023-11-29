import pygame
import sys
from constants import *
from gui_tools import *

# Initializes pygame
pygame.init()

# Initialize custom fonts
title_font = pygame.font.Font(TITLE_FONT, TITLE_FONT_SIZE)
button_font = pygame.font.Font(BUTTON_FONT, BUTTON_FONT_SIZE)
number_font = pygame.font.Font(NUMBER_FONT, NUMBER_FONT_SIZE)

# Initialize pygame screen
view = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Sudoku')

# Fill background color
view.fill(WHITE)

# State keeps track of what menus should be shown. "start" is the start menu and "game" is the sudoku game
state = 'game'


# Draws out title and updates buttons on start menu
def draw_start_menu(mouse_pos):
    # Draw sudoku title at top of screen
    draw_title('Sudoku', y_offset=-110)

    # If mouse is hovering over easy button, change colors
    if draw_button().collidepoint(mouse_pos):
        draw_button(view, button_font, 'easy', button_color=GREY, label_color=WHITE)
    else:
        draw_button(view, button_font, 'easy')

    # If mouse is hovering over medium button, change colors
    if draw_button(y_offset=50).collidepoint(mouse_pos):
        draw_button(view, button_font, 'medium', y_offset=50, button_color=GREY, label_color=WHITE)
    else:
        draw_button(view, button_font, 'medium', y_offset=50)

    # If mouse is hovering over hard button, change colors
    if draw_button(y_offset=100).collidepoint(mouse_pos):
        draw_button(view, button_font, 'hard', y_offset=100, button_color=GREY, label_color=WHITE)
    else:
        draw_button(view, button_font, 'hard', y_offset=100)


def draw_game_board():
    draw_grid(view)

    draw_number(view, number_font, 1, 4, 4)
    draw_number(view, number_font, 2, 4, 5)
    draw_number(view, number_font, 3, 4, 6)
    draw_number(view, number_font, 4, 5, 4)
    draw_number(view, number_font, 5, 5, 5)
    draw_number(view, number_font, 6, 5, 6)
    draw_number(view, number_font, 7, 6, 4)
    draw_number(view, number_font, 8, 6, 5)
    draw_number(view, number_font, 9, 6, 6)


while True:
    # Read and store current mouse position
    mouse_position = pygame.mouse.get_pos()

    if state == 'start':  # Draws out start menu if in start menu
        draw_start_menu(mouse_position)
    elif state == 'game':  # Draws out game board and grid if in game
        draw_game_board()

    for event in pygame.event.get():
        # Closes game when X is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Updates visuals on screen every frame
    pygame.display.update()
