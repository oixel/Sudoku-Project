import pygame

# Initializes pygame
pygame.init()

# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (185, 185, 185)

# Screen size constants
WIDTH = 400
HEIGHT = 400

# Initialize custom fonts
title_font = pygame.font.Font("assets/Nosifer-Regular.ttf", 45)
button_font = pygame.font.Font(None, 25)

# Initialize pygame screen
view = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Sudoku')

# Fill background color
view.fill(WHITE)

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
    # Initialize default button size
    button_width = 80
    button_height = 35

    # Draw rectangle around button label
    button = pygame.Rect(WIDTH / 2 - (button_width / 2) + x_offset, HEIGHT / 2 - (button_height / 2) + y_offset,
                         button_width, button_height)
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

    # Draws out start menu
    start_menu(mouse_position)

    for event in pygame.event.get():
        # Closes game when X is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Updates visuals on screen every frame
    pygame.display.update()
