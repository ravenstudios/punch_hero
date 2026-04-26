from game import Game
from menu import Menu
from pause_menu import PauseMenu
from game_type_menu import GameTypeMenu
from speed_menu import SpeedMenu
from time_menu import TimeMenu

class StateManager:
    def __init__(self, game_context):
        self.states = {
            "menu": Menu(game_context),
            "game": Game(game_context),
            "pause": PauseMenu(game_context),
            "game_type_menu": GameTypeMenu(game_context),
            "speed_menu": SpeedMenu(game_context),
            "time_menu": TimeMenu(game_context),
        }

        self.current = "game"

    def change_state(self, new_state):
        if new_state in self.states:
            self.current = new_state
        else:
            print(f"Unknow State \"{new_state}\"")

    def update(self):
        self.states[self.current].update()

    def draw(self):
        self.states[self.current].draw()

    def reset(self):
        self.states[self.current].reset()
