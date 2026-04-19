class GameContext:
    def __init__(self, surface, input_manager, font):
        self.input_manager = input_manager
        self.surface = surface
        self.font = font
        self.change_state = None