import pygame

class FallingBlock:
    def __init__(self, screen_size, pos):
        self.screen_size = screen_size
        self.gap = self.screen_size[0] // 10
        self.w = self.gap
        self.h = self.w
        self.pos_x = pos[0]

        self.speed = 20
        self.color = (0, 0, 255)
        self.hit_color = (0, 0, 255)

        x = self.gap if pos[0] == 0 else self.screen_size[0] - self.w - self.gap

        self.rect = pygame.Rect(x, -(pos[1] * self.h), self.w, self.h)


    def update(self, falling_blocks):
        # print(len(falling_blocks))
        # print(self.rect)
        self.rect.y += self.speed
        if self.rect.top >= self.screen_size[1]:
            self.remove(falling_blocks)


    def remove(self, falling_blocks):
        falling_blocks.remove(self)


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


    def check_hit(self, hit_boxs, hit):
        if self.rect.top > 0 and self.rect.bottom < self.screen_size[1]:
            if hit == "L" and self.pos_x == 0:
                if self.rect.colliderect(hit_boxs.rect_l):
                    self.color = (0, 255, 0)
                else:
                    self.color = (255, 0, 0)
            if hit == "R" and self.pos_x == 1:
                if self.rect.colliderect(hit_boxs.rect_r):
                    self.color = (0, 255, 0)
                else:
                    self.color = (255, 0, 0)
