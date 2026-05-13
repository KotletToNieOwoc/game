from .game_state import GameState
from entities import Player
import pygame

class PlayingState(GameState):
    def __init__(self):
        self.player1 = Player(100,100,50,50)
        self.player2 = Player(300,100,50,50)

    def update(self, dt):
        self.player1.update(dt)
        self.player2.update(dt)

    def render(self, screen):
        self.player1.render(screen)
        self.player2.render(screen)