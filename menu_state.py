import pygame
import time
from state import State

class MenuState(State):
    def __init__(self, game_context):
        super().__init__(game_context)
        self.options = {"title": "", "state": ""}
        self.selected_index = 0
        self.selected_rect = None


    def activate_selected(self):
        selected = self.options[self.selected_index]
        self.game_context.change_state(selected["state"])


    def update(self):
        hit = self.input_manager.read_hit()

        if hit:
            side, strength = hit

            if side == "BOTH":
                self.activate_selected()
                return

            if side == "L":
                self.selected_index = (self.selected_index - 1) % len(self.options)
            elif side == "R":
                self.selected_index = (self.selected_index + 1) % len(self.options)



    def draw(self):
        for i, option in enumerate(self.options):
            text_surface = self.font.render(option["title"], True, (255, 255, 255))
            rect = text_surface.get_rect()
            self.surface.blit(
                text_surface,
                (self.surface.get_size()[0] // 2 - rect.w // 2, 100 + rect.h * i)
            )

        text_surface = self.font.render(self.options[self.selected_index]["title"], True, (255, 255, 255))
        self.selected_rect = text_surface.get_rect()
        self.selected_rect.y = 100 + self.selected_rect.h * self.selected_index
        self.selected_rect.x = self.surface.get_size()[0] // 2 - self.selected_rect.w // 2
        pygame.draw.rect(self.surface, (255, 255, 255), self.selected_rect, 1)
