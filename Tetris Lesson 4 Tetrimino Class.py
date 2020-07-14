# start this lesson with creating tetriminos in tetrimino file
import pygame, sys
from pygame.locals import *

# NEW import assets from tetris_pieces.py
# IMPORTANT depending on how PyCharm is configured, may need to add this directory
# as a path in project interpreter
from tetris_pieces import *

pygame.init()

# colors RGB
black = (0, 0, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
orange = (255, 100, 10)
red = (255, 0, 0)
green = (0, 255, 0)
purple = (160, 32, 240)
gray = (190, 190, 190)
white = (255, 255, 255)

# store colors as a list
colors = [black, cyan, blue, orange, red, green, purple, gray, white]


# variables for window and tiles
clock = pygame.time.Clock()
FPS = 60
width = 640
height = 480
tile_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris")

# draw board function
def draw_board(board, board_surface):
    for row in range(ROWS):
        for col in range(COLS):
            currentTile = board[row][col]
            tile_x = col * tile_size
            tile_y = row * tile_size
            draw_tile((tile_x, tile_y), currentTile, board_surface)


# draw tile function
def draw_tile(position, tile, surface):
    tile_color = colors[tile]
    rect = Rect(position, (tile_size, tile_size))
    pygame.draw.rect(surface, tile_color, rect)
    pygame.draw.rect(surface, gray, rect.inflate(1, 1), 1)


# draw play area
def draw_play_area(screen_position, screen_surface, board_surface):
    rows_toShow = 20.5
    topY = board_surface.get_height() - rows_toShow * tile_size
    screen_surface.blit(board_surface, screen_position, Rect((0, topY),
                        (board_surface.get_width(), rows_toShow * tile_size)))


# NEW draw tetrimino function
def draw_tetrimino(posX, posY, tetrimino, board_surface):
    topX = posX
    topY = posY
    rows = len(tetrimino)
    cols = len(tetrimino[0])

    for row in range(rows):
        for col in range(cols):
            tile = tetrimino[row][col]
            if tile != 0: # the tile is not black on the game display
                tileX = (topX + col) * tile_size
                tileY = (topY + row) * tile_size
                draw_tile((tileX, tileY), tile, board_surface)


# variables for the board
ROWS = 40
COLS = 10
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
board_surface = pygame.Surface((COLS * tile_size, ROWS * tile_size))


# game states
restart = -1
playing = 0
game_over = 1
game_state = playing

# NEW create first tetrimino
active_tetrimino = Tetrimino()
active_tetrimino.grid_ref = board
active_tetrimino.reset()

# game loop
while True:
    # loop when player is playing game
    while game_state == playing:
        # 60 FPS yeeeee
        clock.tick(FPS)
        # handle user input / events
        for event in pygame.event.get():
            # when user clicks the x button
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # NEW after Tetrimino class finished, this will move the piece down the frame quickly
        active_tetrimino.move(0, 1)

        # fill screen with gray, draw backdrop and play area
        screen.fill(gray)
        draw_board(board, board_surface)

        # IMPORTANT NOTE: below code is for checking that drawing a tetrimino works
        # draw_tetrimino(3, 30, pieces["J"][0], board_surface)

        # NEW drawing a random tetris piece
        draw_tetrimino(active_tetrimino.x, active_tetrimino.y,
                       pieces[active_tetrimino.type][active_tetrimino.rotation], board_surface)

        draw_play_area((10, 10), screen, board_surface)

        pygame.display.update()