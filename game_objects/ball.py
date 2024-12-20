from turtle import Turtle
import random
from utils import configs

MOVEMENT_DISTANCE = 15
X_BORDER_LIMIT = configs.GAME_WIDTH / 2 - 10
Y_BORDER_LIMIT = configs.GAME_HEIGHT / 2 - 10


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.y_direction = 1
        self.x_direction = 1

    def reset_position(self) -> None:
        self.home()
        self.x_direction = random.choice([1, -1])
        self.y_direction = random.choice([1, -1])

    def change_direction(self) -> None:
        if abs(self.ycor()) >= Y_BORDER_LIMIT:
            self.change_y_direction()

    def change_x_direction(self) -> None:
        self.x_direction *= -1

    def change_y_direction(self) -> None:
        self.y_direction *= -1

    def move(self) -> None:
        self.change_direction()
        x_cor = self.xcor() + MOVEMENT_DISTANCE * self.x_direction
        y_cor = self.ycor() + MOVEMENT_DISTANCE * self.y_direction
        new_position = (x_cor, y_cor)
        self.setposition(new_position)
