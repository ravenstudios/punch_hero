import os
from sensors import Sensors
from hit_block import HITBLOCK

os.environ["SDL_VIDEODRIVER"] = "kmsdrm"

import pygame

# pygame.init()
pygame.display.init()

pygame.font.init()

font = pygame.font.SysFont(None, 80)  # default font, size 80


surface = pygame.display.set_mode((800, 600))
# print("driver:", pygame.display.get_driver())
# print("size:", screen.get_size())

clock = pygame.time.Clock()
running = True

width, height = surface.get_size()


sensors = Sensors()
left_hitbox = HITBLOCK(surface.get_size(), 0)
right_hitbox = HITBLOCK(surface.get_size(), 1)



def draw():
    left_hitbox.draw(surface)
    right_hitbox.draw(surface)

def update():
    left_hitbox.update()
    right_hitbox.update()


try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill((0, 0, 0))


        # hit = sensors.read_hit()
        # if hit:
        #     side, strength = hit
        #     if side == "L":
        #         c1 = (255, 0, 0)
        #     elif side == "R":
        #         c2 = (255, 0, 0)

        # pygame.draw.rect(screen, c1, (50, 50, 300, 300))
        # pygame.draw.rect(screen, c2, (400, 50, 300, 300))

        update()
        draw()
    
        # text_surface = font.render(str(left), True, (255, 255, 255))
        # screen.blit(text_surface, (100, 400))

        # text_surface = font.render(str(right), True, (255, 255, 255))
        # screen.blit(text_surface, (400, 400))


        pygame.display.flip()
        clock.tick(60)
finally:
    sensors.close()
    pygame.quit()




