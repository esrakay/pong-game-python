import time
from game_objects.ball import Ball
from game_objects.scoreboard import Scoreboard
from game_objects.player import Player
from game_objects.pongscreen import PongScreen
from utils import configs

DISTANCE_LIMIT = configs.GAME_WIDTH / 2 - 50
X_BORDER_LIMIT = configs.GAME_WIDTH / 2 - 10
PLAYER_1_X_POS = (-configs.GAME_WIDTH / 2 + 30, 0)
PLAYER_2_X_POS = (configs.GAME_WIDTH / 2 - 30, 0)


def main() -> None:
    screen = PongScreen()
    ball = Ball()
    player_1 = Player(PLAYER_1_X_POS)
    player_2 = Player(PLAYER_2_X_POS)
    scoreboard = Scoreboard()
    screen.set_player_controllers(player_1, "w", "s")
    screen.set_player_controllers(player_2, "i", "k")

    game_continues = True
    while game_continues:
        ball.move()
        scoreboard.display_scores(player_1, player_2)
        screen.get_screen().update()
        time.sleep(.04)

        if ball.distance(player_1) < 50 and ball.xcor() <= -DISTANCE_LIMIT or ball.distance(player_2) < 50 and ball.xcor() >= DISTANCE_LIMIT:
            ball.change_x_direction()

        if ball.xcor() >= X_BORDER_LIMIT:
            scoreboard.increase_score(player_1)
            ball.reset_position()

        if ball.xcor() <= -X_BORDER_LIMIT:
            scoreboard.increase_score(player_2)
            ball.reset_position()

    screen.get_screen().exitonclick()


if __name__ == "__main__":
    main()
