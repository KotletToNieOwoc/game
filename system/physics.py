import pygame
from entities import Player

class Physics:
    def movement(self, keys):
        gravity = pygame.Vector2(0,1)

        isJump = False
        isDash = False
        ground_y = 500 - self.height

        keys = pygame.key.get_pressed()  # Gives dictonary where each key has a value of 1 or 0. 1 is pressed, 0 is not pressed.

        if keys[pygame.K_LEFT] and self.position.x > self.velocity.x : 
            self.position.x -= self.velocity.x

        if keys[pygame.K_RIGHT]and self.position.x < 1000 - self.velocity.x - self.width:
            self.position.x += self.velocity.x

        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
        
        else: 
            self.position.y -= self.velocity.y
            self.velocity.y -= gravity.y

            if self.position.y >= ground_y:
                self.velocity.y = 10
                self.position.y = ground_y
                isJump = False

        if not(isDash):
            self.velocity.x = 10
            if keys[pygame.K_LSHIFT]:
                isDash = True
        
        else:
            self.velocity.x = 20

    def world_collision(self, platforms):
        print("collision")

    def player_collision(self):                        
        print("collision")