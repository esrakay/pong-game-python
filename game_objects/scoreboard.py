from turtle import Turtle
from utils import configs

ALIGNMENT = "center"
FONT = ("Arial", 50, "normal")
Y_POSITION = configs.GAME_HEIGHT / 2 + 20


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, Y_POSITION)

    def display_scores(self, player_1, player_2):
        self.clear()
        self.write(arg=f'{player_1.score.get_score()} : {player_2.score.get_score()}', align=ALIGNMENT, font=FONT)

    def increase_score(self, player):
        player.score.increase_score()
