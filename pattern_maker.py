import random


class PatterMaker:
    def __init__(self):
        self.bpm = 120
        self.beat_ms = 60000 / self.bpm
        self.division = 2  # 2 = eighth notes, 4 = sixteenth notes
        self.step_ms = self.beat_ms / self.division




    import random

    def generate_chart(self, bpm, song_length_seconds, density=0.45, offset_ms=0, division=2):
        beat_ms = 60000 / bpm
        step_ms = beat_ms / division

        song_length_ms = song_length_seconds * 1000
        usable_length_ms = song_length_ms - offset_ms

        total_steps = int(usable_length_ms / step_ms)

        chart = []

        for step in range(total_steps):
            if random.random() > density:
                continue

            time_ms = offset_ms + (step * step_ms)
            side = random.choice(["L", "R"])

            chart.append((time_ms, side))

        return chart
