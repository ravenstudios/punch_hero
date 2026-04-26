import pygame, random, math

particles = []

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(2, 7)

        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life = random.randint(20, 1000)
        self.size = random.randint(3, 15)
        self.color = color

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.15
        self.life -= 1
        self.size = max(0, self.size - 0.1)

    def draw(self, screen):
        if self.life > 0 and self.size > 0:
            pygame.draw.circle(
                screen,
                self.color,
                (int(self.x), int(self.y)),
                int(self.size)
            )
