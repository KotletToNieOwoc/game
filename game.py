import time
import pygame
from enum import Enum

class GameState(Enum):
    MAIN_MENU = 1
    PLAYING = 2

UPS = 30
TIME_PER_UPDATE = 1 / UPS

game_state = GameState.PLAYING

def init():
    update_count = 0
    last_update_check_time = time.time()
    last_update_time = time.time()

    while True:
        now = time.time()
        update_time = now - last_update_time
        
        if update_time >= TIME_PER_UPDATE:
            update_time -= TIME_PER_UPDATE
            last_update_time = now
            update_count += 1
            update()
        
        if update_count >= 30:
            update_count = 0
            time_elapsed = now - last_update_check_time
            ups_measured = 30 / time_elapsed
            print("UPS: {:.0f}".format(ups_measured))
            last_update_check_time = now 

def update():
    si = 1
    
    # match game_state:
    #     case GameState.MAIN_MENU:

    #     case GameState.PLAYING:

init()