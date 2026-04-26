import pygame


class MusicPlayer:
    def __init__(self):
        self.file = None
        self.is_playing = False
        self.is_paused = False

        self.bpm = 120
        self.offset_ms = 0

        self.song_start_time = 0
        self.pause_start_time = 0
        self.total_paused_time = 0

    def load(self, file, bpm=120, offset_ms=0):
        self.file = file
        self.bpm = bpm
        self.offset_ms = offset_ms

        pygame.mixer.music.load(file)

    def play(self):
        if self.file is None:
            print("No music file loaded")
            return

        pygame.mixer.music.play()

        self.is_playing = True
        self.is_paused = False

        self.song_start_time = pygame.time.get_ticks()
        self.pause_start_time = 0
        self.total_paused_time = 0

    def stop(self):
        pygame.mixer.music.stop()

        self.is_playing = False
        self.is_paused = False

        self.song_start_time = 0
        self.pause_start_time = 0
        self.total_paused_time = 0

    def pause(self):
        if not self.is_playing or self.is_paused:
            return

        pygame.mixer.music.pause()

        self.is_paused = True
        self.pause_start_time = pygame.time.get_ticks()

    def resume(self):
        if not self.is_paused:
            return

        pygame.mixer.music.unpause()

        paused_amount = pygame.time.get_ticks() - self.pause_start_time
        self.total_paused_time += paused_amount

        self.is_paused = False
        self.pause_start_time = 0

    def update(self):
        # pygame.mixer.music.get_busy() returns False when song is done
        if self.is_playing and not self.is_paused:
            if not pygame.mixer.music.get_busy():
                self.is_playing = False

    def get_raw_song_time(self):
        """
        Returns real audio time in ms since pygame started playing.
        Does NOT include offset.
        """
        if not self.is_playing:
            return 0

        if self.is_paused:
            now = self.pause_start_time
        else:
            now = pygame.time.get_ticks()

        return now - self.song_start_time - self.total_paused_time

    def get_song_time(self):
        """
        Returns gameplay/chart time.
        This is the time your blocks should use.
        """
        return self.get_raw_song_time() - self.offset_ms

    def get_bpm(self):
        return self.bpm

    def get_offset(self):
        return self.offset_ms

    def set_offset(self, offset_ms):
        self.offset_ms = offset_ms

    def adjust_offset(self, amount_ms):
        self.offset_ms += amount_ms

    def get_beat_ms(self):
        return 60000 / self.bpm

    def get_current_beat(self):
        song_time = self.get_song_time()
        return song_time / self.get_beat_ms()
