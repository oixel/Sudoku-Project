import pygame
import sys
from constants import *
import gui_tools

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
state = 'start'


# Draws out title and updates buttons on start menu
def draw_start_menu(mouse_pos):
    # Draw sudoku title at top of screen
    gui_tools.draw_title(view, title_font, 'Sudoku', y_offset=-110)

    # If mouse is hovering over easy button, change colors
    if gui_tools.draw_button(view, button_font).collidepoint(mouse_pos):
        gui_tools.draw_button(view, button_font, 'easy', button_color=GREY, label_color=WHITE)
    else:
        gui_tools.draw_button(view, button_font, 'easy')

    # If mouse is hovering over medium button, change colors
    if gui_tools.draw_button(view, button_font, y_offset=50).collidepoint(mouse_pos):
        gui_tools.draw_button(view, button_font, 'medium', y_offset=50, button_color=GREY, label_color=WHITE)
    else:
        gui_tools.draw_button(view, button_font, 'medium', y_offset=50)

    # If mouse is hovering over hard button, change colors
    if gui_tools.draw_button(view, button_font, y_offset=100).collidepoint(mouse_pos):
        gui_tools.draw_button(view, button_font, 'hard', y_offset=100, button_color=GREY, label_color=WHITE)
    else:
        gui_tools.draw_button(view, button_font, 'hard', y_offset=100)


def draw_game_board():
    gui_tools.draw_grid(view)


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

        if event.type == pygame.MOUSEBUTTONDOWN and state == 'game':
            row, column = gui_tools.get_clicked_cell(mouse_position)
            gui_tools.draw_number(view, number_font, '0', row, column)

        #
        # THIS IS STRICTLY FOR DEBUGGING, DELETE FROM FINAL PRODUCT
        #
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                view.fill(WHITE)
                state = 'game' if state == 'start' else 'start'
        #
        #
        #

    # Updates visuals on screen every frame
    pygame.display.update()
