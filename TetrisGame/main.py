# @Author  : weibin Ma
# @Time    : 10/30/2019
# @title: pythonPJ
# test push
import sys
import pygame
import random
import time
from settings import *
from piece import Piece
from gamewall import GameWall
from gamedisplay import GameDisplay
from gamestate import GameState
def main():

    pygame.init()

    screen = pygame.display.set_mode((1200, 900) )  #resolution ratio 1200*900
    pygame.display.set_caption("TetrisGame")  #window title
    pygame.key.set_repeat(10, 100)

    #background color
    bg_color = (230, 230, 230)

    #create blocks
    #piece = None

    random.seed(int(time.time()))
    #game_wall = GameWall(screen)
    #piece = Piece(random.choice(PIECE_TYPES), screen,game_wall)
    game_state = GameState(screen)

    #main body

    while True:

        if  game_state.piece.is_on_bottom:
            game_state.wall.add_to_wall(game_state.piece)
            game_state.add_score(game_state.wall.eliminate_lines())
            game_state.piece = Piece(random.choice(PIECE_TYPES), screen,game_state.wall)

        check_events(game_state.piece)


        #Fill in the screen background color
        screen.fill(bg_color)


        #draw the wall
        GameDisplay.draw_game_area(screen, game_state)

        #draw block with method
        game_state.piece.paint()

        # make draw visible
        pygame.display.flip()

def check_events(piece):
      '''catch the event'''
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
            elif event.type == pygame.KEYDOWN:
                on_key_down(event,piece)
            elif event.type == pygame.USEREVENT:
                piece.move_down()

def on_key_down(event,piece):

    if event.key == pygame.K_DOWN:
        #print("press aown")
        piece.move_down()
    elif event.key == pygame.K_UP:
        print("press up")
        piece.turn()
    elif event.key == pygame.K_RIGHT:
        # print("press right")
        piece.move_right()
    elif event.key == pygame.K_LEFT:
        #print("press left")
        piece.move_left()
    elif event.key == pygame.K_f:
        piece.fall_down()





# dtaw the game area
'''def draw_game_area(screen):
        #color(rgb), start node, end node

        pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP),
                         (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP))
        # bottom
        for i in range(21):
            pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP + i* CELL_WIDTH),
                         (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + i* CELL_WIDTH))
        # left
        pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP),
                         (GAME_AREA_LEFT, GAME_AREA_TOP + 20 * CELL_WIDTH))
        # right
        for i in range(11):
           pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT + i * CELL_WIDTH, GAME_AREA_TOP),
                         (GAME_AREA_LEFT + i * CELL_WIDTH, GAME_AREA_TOP + 20 * CELL_WIDTH))
'''
'''def draw_cell(screen,left,top):
    
        #left: the length from the window left
        #top: the length from the window top
    
    cell_left_top = (left+ 4*CELL_WIDTH, top)  # block left top

    cell_width_height = (CELL_WIDTH, CELL_WIDTH)  # width and height of bolck

    cell_rect = pygame.Rect(cell_left_top , cell_width_height)  # draw the left-top rect

    pygame.draw.rect(screen, CELL_COLOR, cell_rect)  # draw rect
'''

if __name__ == '__main__':
       main()