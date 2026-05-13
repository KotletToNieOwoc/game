import pygame
from entities import Player

class Input():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def update(self):
        keys = pygame.key.get_pressed()  # Gives dictonary where each key has a value of 1 or 0. 1 is pressed, 0 is not pressed.

        if keys[pygame.K_a] == True:
            self.player1.inputs.left = True
        if keys[pygame.K_d]:
            self.player1.inputs.right = True
        if keys[pygame.K_w]:
            self.player1.inputs.up =  True
        if keys[pygame.K_s]:
            self.player1.inputs.down = True
        if keys[pygame.K_LSHIFT]:
            self.player1.inputs.down = True

        if keys[pygame.K_LEFT]:
            self.player2.inputs.left = True
        if keys[pygame.K_RIGHT]:
            self.player2.inputs.right = True
        if keys[pygame.K_UP]:
            self.player2.inputs.up = True
        if keys[pygame.K_DOWN]:
            self.player2.inputs.down = True
        if keys[pygame.K_RSHIFT]:
            self.player2.inputs.down = True


        