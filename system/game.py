import time
from game_states.playing_state import PlayingState
import pygame

class Game():
    UPS = 30
    TIME_PER_UPDATE = 1 / UPS

    def __init__(self):
        self.game_state = PlayingState()    #sets the initial state of the game to playing 
                                            #(will be main menu ideally later)
        self.run()

    def run(self):
        self.running = True

        update_count = 0
        last_update_check_time = time.time()
        last_update_time = time.time()

        while self.running:
            now = time.time()
            update_time = now - last_update_time

            if update_time >= Game.TIME_PER_UPDATE:
                update_time -= Game.TIME_PER_UPDATE
                last_update_time = now
                update_count += 1
                self.update()
            
            if update_count >= 30:
                update_count = 0
                time_elapsed = now - last_update_check_time
                ups_measured = 30 / time_elapsed
                print("UPS: {:.0f}".format(ups_measured))
                last_update_check_time = now

    def update(self):
        self.game_state.update()

    def render(self):
        self.game_state.render()