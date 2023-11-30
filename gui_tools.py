import pygame
from constants import *


# Draw title at center of screen with given offset
def draw_title(view, font, text, x_offset=0, y_offset=0, color=BLACK):
    title = font.render(text, True, color)
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


# Draw background grid of 9 9x9 grids with varying line widths
def draw_grid(view):
    # Adds extra space created by lines so grid is still accurate
    extra_space = 0

    # Draws horizontal lines
    for i in range(1, ROWS):
        if i % 3 == 0:  # Draws bold grid lines
            extra_space += BOLD_LINE_WIDTH  # Adds line's width to offset to keep everything accurate
            pygame.draw.line(
                view,
                BLACK,
                (0, CELL_SIZE * i + extra_space),
                (WIDTH, CELL_SIZE * i + extra_space),
                BOLD_LINE_WIDTH
            )
        else:  # Draws thinner grid lines
            extra_space += THIN_LINE_WIDTH  # Adds line's width to offset to keep everything accurate
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
        if i % 3 == 0:  # Draws bold grid lines
            extra_space += BOLD_LINE_WIDTH  # Adds line's width to offset to keep everything accurate
            pygame.draw.line(
                view,
                BLACK,
                (CELL_SIZE * i + extra_space, 0),
                (CELL_SIZE * i + extra_space, HEIGHT),
                BOLD_LINE_WIDTH
            )
        else:  # Draws thinner grid lines
            extra_space += THIN_LINE_WIDTH  # Adds line's width to offset to keep everything accurate
            pygame.draw.line(
                view,
                BLACK,
                (CELL_SIZE * i + extra_space, 0),
                (CELL_SIZE * i + extra_space, HEIGHT),
                THIN_LINE_WIDTH
            )


# Calculates extra space needed to account for grid lines' widths
def get_extra_space(num):
    extra_space = 0

    for i in range(1, num):
        if i % 3 == 0:  # Bold lines
            extra_space += BOLD_LINE_WIDTH
        else:  # Thin lines
            extra_space += THIN_LINE_WIDTH

    return extra_space  # Return calculated offset


# Draw given number in specified row and column
def draw_number(view, font, num: str, row, col):
    # Calculates offset that is needed for the number to be centered in cell
    extra_x = get_extra_space(col)
    extra_y = get_extra_space(row)

    # Calculates number's center values
    x = (col * CELL_SIZE) + extra_x - (NUMBER_FONT_SIZE / 2)
    y = (row * CELL_SIZE) + extra_y - (NUMBER_FONT_SIZE / 2)

    # Renders number in desired row and column
    num_surface = font.render(num, 2, BLACK)
    num_rect = num_surface.get_rect(center=(x, y))
    view.blit(num_surface, num_rect)


# Gets row and column of cell that mouse clicks
def get_clicked_cell(mouse_position):
    # Stores count of cells horizontal and vertical from where the mouse is pressed
    # The [0] value represents total cells while the [1] value represents the amount of 3rd cells present
    counts_x = [mouse_position[0] // CELL_SIZE, mouse_position[0] // (CELL_SIZE * 3)]
    counts_y = [mouse_position[1] // CELL_SIZE, mouse_position[1] // (CELL_SIZE * 3)]

    # Math explanation:
    # For every cell that is not followed by a bold line, there is a 3px gap created by the thin lines of the grid
    # For every third cell there is an extra gap of 5px created by the bold lines of the grid
    # So we have to take the difference between the two line widths because otherwise we would be adding
    # an unnecessary +3 pixels to the offset.
    # That way instead of having an incorrect offset of 14, we get a correct offset of 11!
    x_offset = counts_x[0] * THIN_LINE_WIDTH + counts_x[1] * (BOLD_LINE_WIDTH - THIN_LINE_WIDTH)
    y_offset = counts_y[0] * THIN_LINE_WIDTH + counts_y[1] * (BOLD_LINE_WIDTH - THIN_LINE_WIDTH)

    # We add 1 to the row and column locations because we do not have a zero column or row
    # And if we click on the first cell it would normally be 0, 0 without the increment
    row = (mouse_position[1] - y_offset) // CELL_SIZE + 1
    column = (mouse_position[0] - x_offset) // CELL_SIZE + 1

    # Returns clicked row and column!
    return row, column

# Fills cell in given column and row with the desired color
def color_cell(view, col, row, color):
    # Calculates offset that is needed for the blank square to be centered in cell
    extra_x = get_extra_space(row)
    extra_y = get_extra_space(col)

    # Places square in center of cell
    x = (row * CELL_SIZE) - CELL_SIZE + extra_x
    y = (col * CELL_SIZE) - CELL_SIZE + extra_y

    # Draws a square a little bigger than the cell to completely fill cell slot
    pygame.draw.rect(view, color, (x, y, CELL_SIZE + 3, CELL_SIZE + 3))
