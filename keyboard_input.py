import pygame
class KeyboardInput:
    def __init__(self):
        self.error = None
        self.events = None


    def get_events(self, events):
        self.events = events


    def read_hit(self):
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    return ["L", 100]
                if event.key == pygame.K_d:
                    return ["R", 100]
                if event.key == pygame.K_SPACE:
                    return ["BOTH", 100]


    def close(self):
        pass
