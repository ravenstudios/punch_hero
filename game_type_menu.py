from menu_state import MenuState

class GameTypeMenu(MenuState):
    def __init__(self, game_context):
        super().__init__(game_context)
        self.options = [
            {"title":"Game 1", "state": "game"},
            {"title":"Game 2", "state": "game2"},
            {"title":"Speed", "state": "speed_menu"},
            {"title":"Time", "state": "time_menu"},


        ]
