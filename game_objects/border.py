from turtle import Turtle


class Border(Turtle):
    def __init__(self, x_cor, y_cor, head_direction, length):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.shapesize(length, .05)
        self.setheading(head_direction)
        self.penup()
        self.goto(x_cor, y_cor)
