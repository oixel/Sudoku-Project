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

# Variables for typing numbers in
selected_cell = [0, 0]
current_num = ''


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
            # Gets clicked cell's location on grid
            row, column = gui_tools.get_clicked_cell(mouse_position)

            #
            # WHEN FUNCTIONALITY IS BUILT IN MAKE SURE TO SET ORIGINAL NUMBER BACK INSTEAD OF JUST ERASING IT
            #
            if selected_cell != [0, 0]:
                gui_tools.color_cell(view, selected_cell[0], selected_cell[1], WHITE)
                gui_tools.draw_number(view, number_font, current_num, selected_cell[0], selected_cell[1])
                current_num = ''
            #
            #
            #

            # Stores what cell was just clicked on
            selected_cell[0], selected_cell[1] = row, column

            # Sets background color of clicked cell to highlight color
            gui_tools.color_cell(view, row, column, HIGHLIGHT)

        # Called when a key on the keyboard is pressed
        if event.type == pygame.KEYDOWN:
            # If a cell is selected, allow for numbers to be typed
            if selected_cell != [0, 0]:
                match event.key:
                    case pygame.K_BACKSPACE:
                        current_num = ''
                    case pygame.K_1:
                        current_num = '1'
                    case pygame.K_2:
                        current_num = '2'
                    case pygame.K_3:
                        current_num = '3'
                    case pygame.K_4:
                        current_num = '4'
                    case pygame.K_5:
                        current_num = '5'
                    case pygame.K_6:
                        current_num = '6'
                    case pygame.K_7:
                        current_num = '7'
                    case pygame.K_8:
                        current_num = '8'
                    case pygame.K_9:
                        current_num = '9'

                # Wipes previously typed number
                gui_tools.color_cell(view, row, column, HIGHLIGHT)

                # Displays new number in cell
                gui_tools.draw_number(view, number_font, current_num, row, column)

                # If ENTER key is pressed, set background to wipe, write desired number, and unclick cell
                if event.key == pygame.K_RETURN:
                    # Wipes previously typed number
                    gui_tools.color_cell(view, row, column, WHITE)

                    # Displays new number in cell
                    gui_tools.draw_number(view, number_font, current_num, row, column)

                    # Resets values and unclicks cell
                    current_num = ''
                    selected_cell = [0, 0]
                    row = 0
                    column = 0

            #
            # THIS IS STRICTLY FOR DEBUGGING, DELETE FROM FINAL PRODUCT
            #
            if event.key == pygame.K_TAB:
                view.fill(WHITE)
                state = 'game' if state == 'start' else 'start'
            #
            #
            #

    # Updates visuals on screen every frame
    pygame.display.update()
