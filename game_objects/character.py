from turtle import Turtle


class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(5, 1)
        self.penup()
        self.color("white")