from turtle import Turtle


class Border(Turtle):
    def __init__(self, x_cor: int, y_cor: int, head_direction: int, length: int) -> None:
        super().__init__()
        self.shape("square")
        self.color("green")
        self.shapesize(length, .05)
        self.setheading(head_direction)
        self.penup()
        self.goto(x_cor, y_cor)
