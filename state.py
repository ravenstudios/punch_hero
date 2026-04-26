import pygame

class State:
    def __init__(self, game_context):
        self.input_manager = game_context.input_manager
        self.surface = game_context.surface
        self.font = game_context.font
        # self.change_state = game_context.change_state
        self.game_context = game_context

    def update(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass
