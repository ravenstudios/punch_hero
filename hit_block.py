import pygame

class HITBLOCK:
    def __init__(self, screen_size, pos):
        self.screen_size = screen_size
        self.w = self.screen_size[0] // 4
        self.h = self.w
        if pos == 0:
            self.x = 0
        else: 
            self.x = self.screen_size[0] - self.w
        self.y = self.screen_size[1] // 2 - self.h // 2
        self.drop_y = -self.h
        self.speed = 10
        self.color = (0, 0, 255)
        self.hit_color = (0, 0, 255)
        self.border_color = (255, 255, 255)

        self.drop_rect = pygame.Rect(self.x, self.drop_y, self.w, self.h)
        self.hit_rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def update(self):
        self.drop_rect.y += self.speed
        if self.drop_rect.top > self.screen_size[1]:
            self.drop_rect.bottom = - self.h
            self.color = (0, 0, 255)
        

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.drop_rect)
        pygame.draw.rect(surface, self.border_color, self.hit_rect, 1)

    def check_hit(self):
        if self.drop_rect.colliderect(self.hit_rect):
            self.color = (0, 255, 0)
        else:
            self.color = (255, 0, 0)