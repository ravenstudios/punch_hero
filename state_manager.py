from game import Game
from menu import Menu
from pause import Pause


class StateManager:
    def __init__(self, game_context):
        self.states = {
            "menu": Menu(game_context),
            "game": Game(game_context),
            "pause": Pause(game_context),
        }

        self.current = "menu"

    def change_state(self, new_state):
        self.current = new_state

    def update(self):
        self.states[self.current].update()

    def draw(self):
        self.states[self.current].draw()