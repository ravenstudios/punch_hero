import pygame
import state
from hit_block import HITBLOCK

class Game(state.State):
    def __init__(self, game_context):
        super().__init__(game_context)
        self.left_hitbox = HITBLOCK(self.surface.get_size(), 0)
        self.right_hitbox = HITBLOCK(self.surface.get_size(), 1)


    def update(self):
        self.left_hitbox.update()
        self.right_hitbox.update()
        # hit = self.input_manager.read_hit()

        # if hit:
        #     side, strength = hit
        #     if side == "L":
        #         self.left_hitbox.check_hit()
        #     elif side == "R":
        #         self.right_hitbox.check_hit()

        hit = self.input_manager.read_hit()

        if hit:
            side, strength = hit
            if side == "L":
                self.game_context.change_state("menu")
            elif side == "R":
                self.game_context.change_state("pause")


    def draw(self):
        self.left_hitbox.draw(self.surface)
        self.right_hitbox.draw(self.surface)