import pygame

class Player():
    def __init__(self, x, y, width, height):
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.hitbox = pygame.Vector2(width, height)