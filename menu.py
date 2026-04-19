import pygame
import time
import state

class Menu(state.State):
    def __init__(self, game_context):
        super().__init__(game_context)
        self.options = ["Start Game", "Options", "Game 1", "Game 2"]
        self.selected_index = 0
        self.selected_rect = None

        self.pending_side = None
        self.pending_time = 0
        self.pending_window = 0.08   # 80 ms
        self.select_lock_until = 0

    def activate_selected(self):
        selected = self.options[self.selected_index]
        print("SELECTING:", selected)

        if selected == "Start Game":
            self.game_context.change_state("game")
        elif selected == "Options":
            self.game_context.change_state("options")
        elif selected == "Game 1":
            self.game_context.change_state("game1")
        elif selected == "Game 2":
            self.game_context.change_state("game2")

    def update(self):
        now = time.monotonic()

        if now < self.select_lock_until:
            return

        hit = self.input_manager.read_hit()

        if hit:
            side, strength = hit
            print("MENU HIT:", hit)

            # direct BOTH from input manager still works
            if side == "BOTH":
                self.pending_side = None
                self.select_lock_until = now + 0.20
                self.activate_selected()
                return

            # first side hit: store it, don't move yet
            if self.pending_side is None:
                if side in ("L", "R"):
                    self.pending_side = side
                    self.pending_time = now
                return

            # opposite side arrived in time => SELECT
            if (
                side in ("L", "R")
                and side != self.pending_side
                and (now - self.pending_time) <= self.pending_window
            ):
                self.pending_side = None
                self.select_lock_until = now + 0.20
                self.activate_selected()
                return

        # no select happened; if pending hit timed out, use it as nav
        if self.pending_side is not None and (now - self.pending_time) > self.pending_window:
            if self.pending_side == "L":
                self.selected_index = (self.selected_index - 1) % len(self.options)
            elif self.pending_side == "R":
                self.selected_index = (self.selected_index + 1) % len(self.options)

            self.pending_side = None

    def draw(self):
        for i, option in enumerate(self.options):
            text_surface = self.font.render(option, True, (255, 255, 255))
            rect = text_surface.get_rect()
            self.surface.blit(
                text_surface,
                (self.surface.get_size()[0] // 2 - rect.w // 2, 100 + rect.h * i)
            )

        text_surface = self.font.render(self.options[self.selected_index], True, (255, 255, 255))
        self.selected_rect = text_surface.get_rect()
        self.selected_rect.y = 100 + self.selected_rect.h * self.selected_index
        self.selected_rect.x = self.surface.get_size()[0] // 2 - self.selected_rect.w // 2
        pygame.draw.rect(self.surface, (255, 255, 255), self.selected_rect, 1)