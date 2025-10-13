import pygame as pg
from settings import *
from game import Game

def main():
    pg.init()
    pg.display.set_caption("Collection Game")
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    game = Game()
    game.run()

    pg.quit()

if __name__ == "__main__":
    main()