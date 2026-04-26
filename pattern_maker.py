import random


class PatternMaker:
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

            hit_time_ms = offset_ms + (step * step_ms)
            side = random.choice([0, 1])  # 0 = left, 1 = right
            # side = 0
            # IMPORTANT: FallingBlock expects (side, hit_time)
            chart.append((side, hit_time_ms))

        return chart
