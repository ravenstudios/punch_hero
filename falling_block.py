import pygame
from particle import Particle


class FallingBlock:
    def __init__(self, screen_size, pos):
        self.screen_size = screen_size
        self.gap = self.screen_size[0] // 10
        self.w = self.gap
        self.h = self.w
        self.pos_x = pos[0]

        self.speed = 5
        self.color = (0, 0, 255)
        self.hit_color = (0, 0, 255)

        x = self.gap if pos[0] == 0 else self.screen_size[0] - self.w - self.gap

        self.rect = pygame.Rect(x, -(pos[1] * self.h), self.w, self.h)
        self.is_active = True
        self.correct_hit = False

        self.particles = []
        self.start_time = None
        self.explode_delay = 1000
        self.particle_ammount = 50

    def update(self, falling_blocks):
        if not self.correct_hit:
            self.rect.y += self.speed
        if self.rect.top >= self.screen_size[1]:
            self.remove(falling_blocks)


        if self.particles:
            for part in self.particles:
                part.update()

        if self.start_time:
            now = pygame.time.get_ticks()
            if now - self.start_time > self.explode_delay:
                self.remove(falling_blocks)

    def remove(self, falling_blocks):
        falling_blocks.remove(self)


    def draw(self, surface):
        if not self.correct_hit:
            pygame.draw.rect(surface, self.color, self.rect)

        if self.particles:
            for part in self.particles:
                part.draw(surface)


    def check_hit(self, hit_boxs, hit):
        if self.rect.top > 0 and self.rect.bottom < self.screen_size[1] and self.is_active:
            if hit == "L" and self.pos_x == 0:
                if self.rect.colliderect(hit_boxs.rect_l):
                    self.color = (0, 255, 0)
                    self.correct_hit = True
                    self.explode(self.rect, self.color)
                else:
                    self.color = (255, 0, 0)
                    self.is_active = False
            if hit == "R" and self.pos_x == 1:
                if self.rect.colliderect(hit_boxs.rect_r):
                    self.correct_hit = True
                    self.explode(self.rect, self.color)
                    self.is_active = False
                else:
                    self.color = (255, 0, 0)
                    self.is_active = False


    def explode(self, block_rect, color):
        self.start_time = pygame.time.get_ticks()
        center_x = block_rect.centerx
        center_y = block_rect.centery

        for _ in range(self.particle_ammount):
            self.particles.append(Particle(center_x, center_y, color))
