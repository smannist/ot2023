import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

## FONT PATH ##

FONT_PATH = os.path.join("src/fonts", "PressStart2P-Regular.ttf")

## DATABASE ##

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "data", DATABASE_FILENAME)

## GAME WINDOW DIMENSIONS ##

PYGAME_WIDTH = 800
PYGAME_HEIGHT = 900

TETRIS_WIDTH = 300
TETRIS_HEIGHT = 600

## GAME GRID SIZE ##

GAME_GRID_ROWS = 21
GAME_GRID_COLUMNS = 11

## GAME WINDOW POSITIONS ##

CENTER_X = (PYGAME_WIDTH - TETRIS_WIDTH) // 2
CENTER_Y = (PYGAME_HEIGHT - TETRIS_HEIGHT) // 2

## GAME CONFIGS ##

FALL_TIME = 0.0
FALL_SPEED = 0.50

BLOCK_START_X = 5
BLOCK_START_Y = 0

## GAME COLORS ##

COLORS = {"black": (0, 0, 0),
          "cyan": (204, 255, 255),
          "dark_grey": (80, 80, 80),
          "light_grey": (128, 128, 128),
          "S": (0, 255, 0),
          "O": (255, 0, 0),
          "Z": (0, 0, 255),
          "I": (0, 255, 255),
          "L": (255, 0, 255),
          "J": (255, 160, 0),
          "T": (255, 255, 50)}
