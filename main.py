import os
import pygame
from input_manager import InputManager
from state import State
from game_context import GameContext
from state_manager import StateManager
from keyboard_input import KeyboardInput

computer_debug = 1
keyboard_input = KeyboardInput()
if not computer_debug:
    from sensors import Sensors
    sensors = Sensors()

if computer_debug:
    input_manager = InputManager(keyboard_input)
else:
    os.environ["SDL_VIDEODRIVER"] = "kmsdrm"
    input_manager = InputManager(sensors)


pygame.display.init()
pygame.font.init()

font = pygame.font.SysFont(None, 80)  # default font, size 80
surface = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
width, height = surface.get_size()


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
        events = pygame.event.get()
        keyboard_input.get_events(events)
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        update()
        draw()


# except Exception as e:
#     print("CRASH:", e)

finally:
    input_manager.close()
    pygame.quit()
