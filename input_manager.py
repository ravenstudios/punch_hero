from sensors import Sensors


class INPUT_MANAGER:
    def __init__(self):
        self.sensors = Sensors()
        self.error = self.sensors.error
    

    def update(self):
        pass
    
    def read_hit(self):
        return self.sensors.read_hit()

    def close(self):
        self.sensors.close()