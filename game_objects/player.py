from game_objects.character import Character
from .score import Score
from utils import configs

MOVEMENT_DISTANCE = 20
Y_BORDER_LIMIT = configs.GAME_HEIGHT / 2 - 50


class Player(Character):
    def __init__(self, start_position):
        super().__init__()
        self.start_position = start_position
        self.reset_position()
        self.score = Score()

    def reset_position(self):
        self.goto(self.start_position)

    def set_y_pos(self, distance):
        y_cor = max(-Y_BORDER_LIMIT, min(Y_BORDER_LIMIT, self.ycor() + distance))
        new_position = (self.xcor(), y_cor)
        self.setposition(new_position)

    def up(self):
        self.set_y_pos(MOVEMENT_DISTANCE)

    def down(self):
        self.set_y_pos(-MOVEMENT_DISTANCE)