from menu_state import MenuState

class PauseMenu(MenuState):
    def __init__(self, game_context):
        super().__init__(game_context)
        self.options = [
            {"title":"Pause", "state": ""},
            {"title":"Back", "state": "game"},
        ]
