import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

VIEW_WIDTH = 400
VIEW_HEIGHT = 400

view = pygame.display.set_mode((VIEW_HEIGHT, VIEW_WIDTH))
pygame.display.set_caption('Sudoku')

title_font = pygame.font.Font("assets/Nosifer-Regular.ttf", 45)
font = pygame.font.Font(None, 25)


def draw_test_title():
    view.fill(WHITE)

    title = title_font.render('Sudoku', True, BLACK)
    title_rect = title.get_rect(center=(VIEW_WIDTH / 2, VIEW_HEIGHT / 2 - 110))
    view.blit(title, title_rect)

#def draw_button(x, y):

while True:
    draw_test_title()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            quit()

    pygame.display.update()
