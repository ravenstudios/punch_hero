import time

class InputManager:
    def __init__(self, input_source):

        self.sensors = input_source
        self.error = self.sensors.error

        self.last_left_time = 0
        self.last_right_time = 0
        self.both_window = 0.05
        self.last_hit_type = None  # "L", "R", or "BOTH"

        self.pending_side = None
        self.pending_time = 0
        self.pending_window = 0.08   # 80 ms
        self.select_lock_until = 0
        self.lock_out_time = 0.20

    def update(self):
        pass


    def read_hit(self):
        hit = self.sensors.read_hit()
        if not hit:
            self.last_hit_type = None
            return

        side, strength = hit
        now = time.monotonic()

        if side == "L":
            self.last_left_time = now
        elif side == "R":
            self.last_right_time = now

        # 👇 detect BOTH
        if abs(self.last_left_time - self.last_right_time) < self.both_window:
            self.last_hit_type = "BOTH"
        else:
            self.last_hit_type = side

        return [self.last_hit_type, strength]

    def read_menu_hit(self):
        now = time.monotonic()

        if now < self.select_lock_until:
            return

        hit = self.read_hit()

        if hit:
            side, strength = hit
            # direct BOTH from input manager still works
            if side == "BOTH":
                self.pending_side = None
                self.select_lock_until = now + self.lock_out_time
                return "BOTH"

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
                self.select_lock_until = now + self.lock_out_time
                return "BOTH"

        # no select happened; if pending hit timed out, use it as nav
        if self.pending_side is not None and (now - self.pending_time) > self.pending_window:
            if self.pending_side == "L":
                return "L"
            elif self.pending_side == "R":
                return "R"

            self.pending_side = None

    def close(self):
        self.sensors.close()
