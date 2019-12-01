# @Author  : weibin Ma
# @Time    : 10/30/2019
# @title: pythonPJ
# test push
import random
from settings import *
from piece import Piece
from gamewall import GameWall
import pygame
class GameState():
    def __init__(self, screen):
        self.screen = screen
        self.wall = GameWall(screen)
        self.piece = None #Piece(random.choice(PIECE_TYPES), screen, self.wall)
        self.timer_interval = TIMER_INTERVAL   #1000ms
        #self.set_timer(self.timer_interval)
        self.game_score = 0
        self.stopped = True

    def set_timer(self, timer_interval):
        self.game_timer = pygame.time.set_timer(pygame.USEREVENT, timer_interval)

    def add_score(self, score):
        self.game_score += score

    def start_game(self):
        self.stopped = False
        self.set_timer(TIMER_INTERVAL)
        self.timer_interval = TIMER_INTERVAL
        self.piece = Piece(random.choice(PIECE_TYPES), self.screen, self.wall)