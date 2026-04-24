import pygame
import state
from hit_boxes import HitBoxes
from falling_block import FallingBlock

class Game(state.State):
    def __init__(self, game_context):
        super().__init__(game_context)
        self.hit_boxes = HitBoxes(self.surface.get_size())
        self.patterns = [(0, 100), (1, 80), (1, 90), (0, 75), (0, 65), (1, 60), (0, 55), (1, 50), (0, 45), (1, 40), (1, 30), (0, 25), (0, 20), (1, 15), (1, 10), (0, 5), (1, 0)]
        self.falling_blocks = []

        for p in self.patterns:
            self.falling_blocks.append(FallingBlock(self.surface.get_size(), p))
        self.hit = None


    def update(self):
        self.hit_boxes.update()
        self.hit = self.input_manager.read_hit()

        if self.hit:
            side, strength = self.hit
            if side == "BOTH":
                self.game_context.change_state("pause")

            for block in self.falling_blocks:
                block.check_hit(self.hit_boxes, self.hit[0])

        for block in self.falling_blocks:
            block.update(self.falling_blocks)



    def draw(self):
        self.hit_boxes.draw(self.surface)
        for block in self.falling_blocks:
            block.draw(self.surface)
