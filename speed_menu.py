from menu_state import MenuState

class SpeedMenu(MenuState):
    def __init__(self, game_context):
        super().__init__(game_context)
        self.options = [
            {"title":"Speed", "state": ""},
            {"title":"Back", "state": "game_type_menu"},


        ]
