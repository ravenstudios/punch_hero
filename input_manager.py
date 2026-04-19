from sensors import Sensors
import time

class InputManager:
    def __init__(self):
        self.sensors = Sensors()
        self.error = self.sensors.error
        
        self.last_left_time = 0
        self.last_right_time = 0
        self.both_window = 0.05
        self.last_hit_type = None  # "L", "R", or "BOTH"


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

    def close(self):
        self.sensors.close()

  
        