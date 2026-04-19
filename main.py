import os
import pygame
from input_manager import INPUT_MANAGER
from state import State, GameContext

from state_manager import StateManager


os.environ["SDL_VIDEODRIVER"] = "kmsdrm"

pygame.display.init()
pygame.font.init()

font = pygame.font.SysFont(None, 80)  # default font, size 80
surface = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

width, height = surface.get_size()

input_manager = INPUT_MANAGER()


game_context = GameContext(surface, input_manager, font)
state_manager = StateManager(game_context)
game_context.change_state = state_manager.change_state



def draw():
    surface.fill((0, 0, 0))
    if input_manager.error:
        text_surface = font.render("Sensor Error", True, (255, 255, 255))
        surface.blit(text_surface, (400, 400))
    else:
        state_manager.draw()

    pygame.display.flip()

def update():
    if input_manager.error:
        return
    state_manager.update()

        
try:
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        update()
        draw()
        

except Exception as e:
    print("CRASH:", e)

finally:
    input_manager.close()
    pygame.quit()




