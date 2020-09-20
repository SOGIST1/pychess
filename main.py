import pygame
import math
# Initializing Pygame
pygame.init()

# Screen
ROWS = 8
WIDTH = 70*ROWS
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("PyChess")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BROWN = (160, 82, 45)
TAN = (222, 184, 135)

# Images
# TODO scale correctly
SCALE = (60, 60)

P_IMAGE = pygame.transform.scale(pygame.image.load("images/pawn.png"), SCALE)
N_IMAGE = pygame.transform.scale(pygame.image.load("images/knight.png"), SCALE)
B_IMAGE = pygame.transform.scale(pygame.image.load("images/bishop.png"), SCALE)
R_IMAGE = pygame.transform.scale(pygame.image.load("images/rook.png"), SCALE)
Q_IMAGE = pygame.transform.scale(pygame.image.load("images/queen.png"), SCALE)
K_IMAGE = pygame.transform.scale(pygame.image.load("images/king.png"), SCALE)

X_IMAGE = pygame.transform.scale(pygame.image.load("images/pawn.png"), SCALE)
O_IMAGE = pygame.transform.scale(pygame.image.load("images/rook.png"), SCALE)

# Fonts
END_FONT = pygame.font.SysFont('courier', 40)


def draw_grid():
    gap = WIDTH // ROWS

    # Starting points
    x = 0
    y = 0

    for i in range(ROWS):
        if i % 2 == 1:
            pygame.draw.rect(screen, BROWN, (x, y, gap, gap))
            x += gap
        for j in range(ROWS // 2):
            pygame.draw.rect(screen, TAN, (x, y, gap, gap))
            x += gap
            pygame.draw.rect(screen, BROWN, (x, y, gap, gap))
            x += gap
        y += gap
        x = 0


def initialize_grid():
    dis_to_cen = WIDTH // ROWS // 2

    # Initializing the array
    game_array = [[None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None]]

    # Mouse position



# Checking if someone has won
def has_won(game_array):
    # Checking rows
    for row in range(len(game_array)):
        if (game_array[0][2] == game_array[1][2] == game_array[2][2]) and game_array[0][2] != "":
            display_message(game_array[0][2].upper() + " has won!")
            return True

    # Checking columns
    for col in range(len(game_array)):
        if (game_array[0][2] == game_array[1][2] == game_array[2][2]) and game_array[0][2] != "":
            display_message(game_array[0][2].upper() + " has won!")
            return True

    # Checking main diagonal
    if (game_array[0][0][2] == game_array[1][1][2] == game_array[2][2][2]) and game_array[0][0][2] != "":
        display_message(game_array[0][0][2].upper() + " has won!")
        return True

    # Checking reverse diagonal
    if (game_array[0][2][2] == game_array[1][1][2] == game_array[2][0][2]) and game_array[0][2][2] != "":
        display_message(game_array[0][2][2].upper() + " has won!")
        return True

    return False


def display_message(content):
    pygame.time.delay(500)
    end_text = END_FONT.render(content, 1, BLACK)
    screen.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(3000)


def render():
    screen.fill(WHITE)
    draw_grid()


def main():
    global x_turn, o_turn, images, draw

    images = []
    draw = False

    run = True

    x_turn = True
    o_turn = False

    game_array = initialize_grid()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(game_array)

        render()

        # TODO win condition sets run to false


while True:
    if __name__ == '__main__':
        main()
