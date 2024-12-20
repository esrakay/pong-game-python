from turtle import Screen
from game_objects.border import Border
from utils import configs
from .player import Player


class PongScreen:
    def __init__(self) -> None:
        self.screen = Screen()
        self.screen.setup(width=configs.SCREEN_WIDTH, height=configs.SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.listen()
        self.screen.tracer(0)
        self.set_borders()

    def set_borders(self) -> None:
        # Top Border
        Border(0, configs.GAME_HEIGHT / 2, 90, configs.GAME_WIDTH / 2 / 10)
        # Bottom Border
        Border(0, -configs.GAME_HEIGHT / 2, 90, configs.GAME_WIDTH / 2 / 10)
        # Left Border
        Border(-configs.GAME_WIDTH / 2, 0, 0, configs.GAME_HEIGHT / 2 / 10)
        # Right Border
        Border(configs.GAME_WIDTH / 2, 0, 0, configs.GAME_HEIGHT / 2 / 10)

    def get_screen(self) -> Screen:
        return self.screen

    def set_player_controllers(self, player: Player, key_up: str, key_down: str) -> None:
        self.screen.onkeypress(player.up, key_up)
        self.screen.onkeypress(player.down, key_down)

