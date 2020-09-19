import pygame as pyg
# Initialize Pygame
pyg.init()

# Screen
pyg.RESIZABLE
WIDTH = 700
ROWS = 8
screen = pyg.display.set_mode([WIDTH, WIDTH])
pyg.display.set_caption("PyChess")

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BROWN = (139,69,19)

# Images
P_IMAGE = pyg.transform.scale(pyg.image.load("images/pawn.png"), (100,100))
N_IMAGE = pyg.transform.scale(pyg.image.load("images/knight.png"), (100,100))
B_IMAGE = pyg.transform.scale(pyg.image.load("images/bishop.png"), (100,100))
R_IMAGE = pyg.transform.scale(pyg.image.load("images/rook.png"), (100,100))
Q_IMAGE = pyg.transform.scale(pyg.image.load("images/queen.png"), (100,100))
K_IMAGE = pyg.transform.scale(pyg.image.load("images/king.png"), (100,100))

#Fonts
