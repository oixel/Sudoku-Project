import pygame
from constants import *

# Initializes pygame
pygame.init()

# Initialize custom fonts
title_font = pygame.font.Font(TITLE_FONT, TITLE_FONT_SIZE)
button_font = pygame.font.Font(BUTTON_FONT, BUTTON_FONT_SIZE)

# Initialize pygame screen
view = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Sudoku')

# Fill background color
view.fill(WHITE)

# State keeps track of what menus should be shown. "start" is the start menu and "game" is the sudoku game
state = 'start'

# Draws out title and updates buttons on start menu
def start_menu(mouse_pos):
    # Draw sudoku title at top of screen
    draw_title('Sudoku', y_offset=-110)

    # If mouse is hovering over easy button, change colors
    if draw_button().collidepoint(mouse_pos):
        draw_button('easy', button_color=GREY, label_color=WHITE)
    else:
        draw_button('easy')

    # If mouse is hovering over medium button, change colors
    if draw_button(y_offset=50).collidepoint(mouse_pos):
        draw_button('medium', y_offset=50, button_color=GREY, label_color=WHITE)
    else:
        draw_button('medium', y_offset=50)

    # If mouse is hovering over hard button, change colors
    if draw_button(y_offset=100).collidepoint(mouse_pos):
        draw_button('hard', y_offset=100, button_color=GREY, label_color=WHITE)
    else:
        draw_button('hard', y_offset=100)


# Draw title at center of screen with given offset
def draw_title(text, x_offset=0, y_offset=0, color=BLACK):
    title = title_font.render(text, True, color)
    title_rect = title.get_rect(center=(WIDTH / 2 + x_offset, HEIGHT / 2 + y_offset))
    view.blit(title, title_rect)


# Draws button with given text label at set offset and with set colors
def draw_button(text='', x_offset=0, y_offset=0, label_color=WHITE, button_color = BLACK):

    # Draw rectangle around button label
    button = pygame.Rect(WIDTH / 2 - (BUTTON_WIDTH / 2) + x_offset, HEIGHT / 2 - (BUTTON_HEIGHT / 2) + y_offset,
                         BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(view, button_color, button)

    # Draw label on top of rectangle
    label = button_font.render(text, True, label_color)
    label_rect = label.get_rect(center=(WIDTH / 2 + x_offset, HEIGHT / 2 + y_offset))
    view.blit(label, label_rect)

    # Return rectangle to check position
    return button


while True:
    # Read and store current mouse position
    mouse_position = pygame.mouse.get_pos()

    if state == 'start': # Draws out start menu if in start menu
        start_menu(mouse_position)

    for event in pygame.event.get():
        # Closes game when X is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Updates visuals on screen every frame
    pygame.display.update()
