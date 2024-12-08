from game_objects.character import Character
from utils import configs

MOVEMENT_DISTANCE = 20
START_POSITION = (configs.GAME_WIDTH / 2 - 30, 0)
Y_BORDER_LIMIT = configs.GAME_HEIGHT / 2 - 50


class NPC(Character):
    def __init__(self):
        super().__init__()
        self.goto(START_POSITION)
        self.direction = 1

    def reset_position(self):
        self.goto(START_POSITION)

    def change_direction(self):
        if self.ycor() >= Y_BORDER_LIMIT or self.ycor() <= -Y_BORDER_LIMIT:
            self.direction *= -1

    def move(self, ball):
        self.change_direction()
        y_cor = self.ycor() + MOVEMENT_DISTANCE * self.direction
        new_position = (self.xcor(), y_cor)
        self.setposition(new_position)

