import pygame
import time
from menu_state import MenuState

class TimeMenu(MenuState):
    def __init__(self, game_context):
        super().__init__(game_context)
        self.options = [
            {"title":"Time", "state": ""},
            {"title":"Back", "state": "game_type_menu"},
        ]
