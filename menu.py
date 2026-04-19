import pygame
import state

class Menu(state.State):
    def __init__(self, game_context):
        super().__init__(game_context)

    def update(self):
        hit = self.input_manager.read_hit()

        if hit:
            side, strength = hit
            if side == "L":
                self.game_context.change_state("pause")
            elif side == "R":
                self.game_context.change_state("game")

    def draw(self):
        text_surface = self.font.render("Menu", True, (255, 255, 255))
        self.surface.blit(text_surface, (400, 400))