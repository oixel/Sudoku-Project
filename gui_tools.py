import pygame
from constants import *


def draw_grid(view):
    # Adds extra space created by lines so grid is still accurate
    extra_space = 0

    # Draws horizontal lines
    for i in range(1, ROWS):
        if i % 3 == 0:  # Draws bold lines
            extra_space += BOLD_LINE_WIDTH
            pygame.draw.line(
                view,
                BLACK,
                (0, CELL_SIZE * i + extra_space),
                (WIDTH, CELL_SIZE * i + extra_space),
                BOLD_LINE_WIDTH
            )
        else:  # Draws thinner lines
            extra_space += THIN_LINE_WIDTH
            pygame.draw.line(
                view,
                BLACK,
                (0, CELL_SIZE * i + extra_space),
                (WIDTH, CELL_SIZE * i + extra_space),
                THIN_LINE_WIDTH
            )

    extra_space = 0  # Resets extra space

    # Draws vertical lines
    for i in range(1, ROWS):
        if i % 3 == 0:  # Draws bold lines
            extra_space += BOLD_LINE_WIDTH
            pygame.draw.line(
                view,
                BLACK,
                (CELL_SIZE * i + extra_space, 0),
                (CELL_SIZE * i + extra_space, HEIGHT),
                BOLD_LINE_WIDTH
            )
        else:  # Draws thinner lines
            extra_space += THIN_LINE_WIDTH
            pygame.draw.line(
                view,
                BLACK,
                (CELL_SIZE * i + extra_space, 0),
                (CELL_SIZE * i + extra_space, HEIGHT),
                THIN_LINE_WIDTH
            )


def get_extra_space(num):
    extra_space = 0

    for i in range(1, num):
        if i % 3 == 0:
            print('run')
            extra_space += BOLD_LINE_WIDTH
        else:
            print('run', i)
            extra_space += THIN_LINE_WIDTH

    print(extra_space)
    return extra_space


def draw_number(view, font, num, row, col):
    extra_x = get_extra_space(col)
    extra_y = get_extra_space(row)

    num_surface = font.render(str(num), 2, BLACK)
    x = col * CELL_SIZE + extra_x - (NUMBER_FONT_SIZE / 2)
    y = row * CELL_SIZE + extra_y - (NUMBER_FONT_SIZE / 2)
    num_rect = num_surface.get_rect(center=(x, y))
    view.blit(num_surface, num_rect)


# Draw title at center of screen with given offset
def draw_title(text, x_offset=0, y_offset=0, color=BLACK):
    title = title_font.render(text, True, color)
    title_rect = title.get_rect(center=(WIDTH / 2 + x_offset, HEIGHT / 2 + y_offset))
    view.blit(title, title_rect)


# Draws button with given text label at set offset and with set colors
def draw_button(view, font, text='', x_offset=0, y_offset=0, label_color=WHITE, button_color = BLACK):

    # Draw rectangle around button label
    button = pygame.Rect(WIDTH / 2 - (BUTTON_WIDTH / 2) + x_offset, HEIGHT / 2 - (BUTTON_HEIGHT / 2) + y_offset,
                         BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(view, button_color, button)

    # Draw label on top of rectangle
    label = font.render(text, True, label_color)
    label_rect = label.get_rect(center=(WIDTH / 2 + x_offset, HEIGHT / 2 + y_offset))
    view.blit(label, label_rect)

    # Return rectangle to check position
    return button
