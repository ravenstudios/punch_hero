import pygame

class HitBoxes:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.gap = self.screen_size[0] // 10
        self.w = self.gap
        self.h = self.w
        self.y = self.screen_size[1] - self.h - self.gap
        self.color = (255, 255, 255)
        self.rect_l = pygame.Rect(self.gap, self.y, self.w, self.h)
        x = self.screen_size[0] - self.w - self.gap
        self.rect_r = pygame.Rect(x, self.y, self.w, self.h)

    def update(self):
        pass


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect_l, 1)
        pygame.draw.rect(surface, self.color, self.rect_r, 1)

    def check_hit(self, hit):
        pass
