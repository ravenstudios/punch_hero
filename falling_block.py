import pygame
from particle import Particle


class FallingBlock:
    def __init__(self, screen_size, pos, hit_y, fall_time_ms=2000):
        self.screen_size = screen_size
        self.gap = self.screen_size[0] // 10
        self.w = self.gap
        self.h = self.w

        self.pos_x = pos[0]          # 0 = left, 1 = right
        self.hit_time = pos[1]       # ms when block should reach hit box

        self.hit_y = hit_y
        self.spawn_y = -self.h
        self.fall_time_ms = fall_time_ms

        self.color = (0, 0, 255)
        self.hit_color = (0, 255, 0)

        x = self.gap if self.pos_x == 0 else self.screen_size[0] - self.w - self.gap
        self.rect = pygame.Rect(x, self.spawn_y, self.w, self.h)

        self.is_active = True
        self.correct_hit = False
        self.missed = False

        self.particles = []
        self.start_time = None
        self.explode_delay = 1000
        self.particle_ammount = 50

        self.hit_window_size = self.rect.h // 2


    def update(self, falling_blocks, hit_boxs, song_time):
        if not self.correct_hit:
            time_until_hit = self.hit_time - song_time

            progress = 1 - (time_until_hit / self.fall_time_ms)

            # Let it go past hit line after miss
            progress = max(0, min(1.5, progress))

            self.rect.y = int(
                self.spawn_y + progress * (self.hit_y - self.spawn_y)
            )

        if self.rect.y > hit_boxs.rect_l.bottom:
            self.is_active = False
        # Remove if it falls off screen
        if self.rect.top >= self.screen_size[1]:
            self.remove(falling_blocks)
            return -1

        for part in self.particles:
            part.update()

        if self.start_time:
            now = pygame.time.get_ticks()
            if now - self.start_time > self.explode_delay:
                self.remove(falling_blocks)
        return 0

    def remove(self, falling_blocks):
        if self in falling_blocks:
            falling_blocks.remove(self)

    def draw(self, surface):
        if not self.correct_hit:
            pygame.draw.rect(surface, self.color, self.rect)

        for part in self.particles:
            part.draw(surface)

    def check_hit(self, hit_boxs, hit):
        if not self.is_active or self.correct_hit:
            return 0

        if hit == "L" and self.pos_x == 0:
            hit_center = hit_boxs.rect_l.centery
            block_center = self.rect.centery

            if abs(block_center - hit_center) < self.hit_window_size:
                # good hit
            # if self.rect.colliderect(hit_boxs.rect_l):
                self.correct_hit = True
                self.explode(self.rect.copy(), self.hit_color)
                return 1
            else:
                return -1

        elif hit == "R" and self.pos_x == 1:
            if self.rect.colliderect(hit_boxs.rect_r):
                self.correct_hit = True
                self.explode(self.rect.copy(), self.hit_color)
                return 1
            else:
                return -1


        return 0

    def explode(self, block_rect, color):
        self.start_time = pygame.time.get_ticks()
        center_x = block_rect.centerx
        center_y = block_rect.centery

        for _ in range(self.particle_ammount):
            self.particles.append(Particle(center_x, center_y, color))
