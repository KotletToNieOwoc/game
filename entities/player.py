import pygame
from enum import Enum

class Direction(Enum):
    LEFT = -1
    RIGHT = 1

class AttackType(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2

class InputValues():
    left = False
    right = False
    up = False
    down = False
    dash = False

class Attack():
    def __init__():
        self.delay
        self.timeActive
        self.duration
        self.destroy = False
        self.activated = False
        self.hitbox
        self.position
    
    def update(self, dt):
        self.timeActive += dt
        if self.timeActive >= self.delay and not self.activated:
            activated = True
        if self.timeActive >= self.duration:
            destroy = True

        #moves with the player

        if self.activated:
            Physics.playerCollision(self, )

        

class Player():
    attacks = []
    blocking = False
    crouch = False
    dash_cooldown = 0

    def __init__(self, x, y, width, height):
        self.inputs = InputValues() # left, right, up, down
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.hitbox = pygame.Vector2(width, height)
        self.facing_direction = Direction.RIGHT
    
    def update(self, dt):
        #Physics.move(self, dt)
        
        for index, attack in enumerate(self.attacks):
            attack.update()
            if attack.destroy:
                self.attacks.pop(index)

    def attacked(type):
        match type:
            case AttackType.HIGH:
                #check blocking
                pass
            case AttackType.MEDIUM:
                pass
            case AttackType.LOW:
                pass

    def attack(self):
        pass

    def render(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.position.x, self.position.y, self.hitbox.x, self.hitbox.y))  #This takes: window/surface, color, rect 