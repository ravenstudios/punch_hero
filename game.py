import pygame
import state
from hit_boxes import HitBoxes
from falling_block import FallingBlock
from music_player import MusicPlayer
from pattern_maker import PatternMaker


class Game(state.State):
    def __init__(self, game_context):
        super().__init__(game_context)

        self.hit_boxes = HitBoxes(self.surface.get_size())

        self.music_player = MusicPlayer()
        self.pattern_maker = PatternMaker()

        self.bpm = 134
        self.song_length_seconds = 222
        self.offset_ms = 4000
        self.density = 1
        self.division = 0.5
        beat_ms = 60000 / self.bpm
        self.fall_time_ms = beat_ms * 4
        self.score = 0

        # self.fall_time_ms = 2000

        self.chart = self.pattern_maker.generate_chart(
            bpm=self.bpm,
            song_length_seconds=self.song_length_seconds,
            density=self.density,
            offset_ms=self.offset_ms,
            division=self.division
        )

        self.chart_index = 0
        self.falling_blocks = []
        self.hit = None

        self.music_player.load(
            "songs/Mortal Kombat Theme Song.mp3",
            bpm=self.bpm,
            offset_ms=self.offset_ms
        )

        self.music_player.play()

    def spawn_blocks(self, song_time):
        hit_y = self.hit_boxes.rect_l.y

        while self.chart_index < len(self.chart):
            side, hit_time = self.chart[self.chart_index]

            # Spawn when block should enter from top
            if song_time >= hit_time - self.fall_time_ms:
                block = FallingBlock(
                    self.surface.get_size(),
                    (side, hit_time),
                    hit_y=hit_y,
                    fall_time_ms=self.fall_time_ms
                )

                self.falling_blocks.append(block)
                self.chart_index += 1
            else:
                break

    def update(self):
        self.hit_boxes.update()
        self.music_player.update()

        # Use raw song time because chart already includes offset
        song_time = self.music_player.get_raw_song_time()

        self.spawn_blocks(song_time)

        self.hit = self.input_manager.read_hit()

        if self.hit:
            side, strength = self.hit

            if side == "BOTH":
                self.game_context.change_state("pause")
                return

            for block in self.falling_blocks:
                result = block.check_hit(self.hit_boxes, side)

                if result == 0:
                    continue   # this block did not care about this hit

                self.score += result
                break

        for block in self.falling_blocks[:]:
            self.score += block.update(self.falling_blocks, self.hit_boxes, song_time)

    def draw(self):
        self.hit_boxes.draw(self.surface)

        for block in self.falling_blocks:
            block.draw(self.surface)

        text_surface = self.font.render(f"Score:{self.score}", True, (255, 255, 255))
        rect = text_surface.get_rect()
        self.surface.blit(
            text_surface,
            (self.surface.get_size()[0] // 2 - rect.w // 2, 50)
        )

    def reset(self):
        self.falling_blocks = []
        self.chart_index = 0
        self.music_player.stop()
        self.music_player.play()
