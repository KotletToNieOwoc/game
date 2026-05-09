import pygame
from player import Player

pygame.init()

screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("First Game")

position = pygame.math.Vector2(50,435)
velocity = pygame.math.Vector2(5,10)

width = 40
height = 60

isJump = False
isDash = False
jumpCount = 10
no_collision = True

run = True

while run:
    pygame.time.delay(100) # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay

    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop

    keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

    if keys[pygame.K_LSHIFT]:
        velocity.x = 10

    if keys[pygame.K_LEFT] and pos.x > vel.x : 
        position.x -= velocity.x

    if keys[pygame.K_RIGHT]and pos.x < 1000 - vel.x - width:
        position.x += vel.x

    if not(isJump):
        if keys[pygame.K_UP]and pos.y > vel.y:
            pos.y -= vel.y

        if keys[pygame.K_DOWN]and pos.y < 500 - vel.y - height:
            pos.y += vel.y

        if keys[pygame.K_SPACE]:
            isJump = True
    
    else: 
        pos.y -= vel.y
        vel.y -= 1

        if vel.y < -10:
            vel.y = 10
            isJump = False
                
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), (pos.x, pos.y, width, height))  #This takes: window/surface, color, rect 
    pygame.display.update() # This updates the screen so we can see our rectangle

pygame.quit()  # If we exit the loop this will execute and close our game