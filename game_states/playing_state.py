from .game_state import GameState
from entities import Player
import pygame

class PlayingState(GameState):
    def __init__(self):
        self.player1 = Player(100,100,50,50)
        self.player2 = Player(300,100,50,50)

    def update(self):
        self.player1.update()
        self.player2.update()

    def render(self):
        pass