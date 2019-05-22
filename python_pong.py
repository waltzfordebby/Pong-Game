# Importing modules
from turtle import Turtle, Screen
import os

# This is the paddle class
class Paddle(Turtle):
    def __init__(self, shape, color, position):
        Turtle.__init__(self)
        self.shape(shape)
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.score = 0

    # Move the paddle up
    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)
        self.check_border_collision()

    # Move the paddle down
    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)
        self.check_border_collision()


    def check_border_collision(self):
        if self.ycor() > 250:
            self.sety(250)

        if self.ycor() < -250:
            self.sety(-250)
 
        

# This the ball class
class Ball(Turtle):
    def __init__(self, shape, color):
        Turtle.__init__(self)
        self.shape(shape)
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(0, 0)
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.dx = 1
        self.dy = 1

    def check_border_collision(self, paddle_a, paddle_b):
        if self.ycor() > 290:
            self.sety(290)
            self.dy *= -1

        if self.ycor() < -290:
            self.sety(-290)
            self.dy *= -1

        if self.xcor() > 390:
            self.goto(0, 0)
            self.dx *= -1
            paddle_a.score += 1
            os.system("aplay bounce.wav&")

        if self.xcor() < -390:
            self.goto(0, 0)
            self.dx *= -1
            paddle_b.score +=1
            os.system("aplay bounce.wav&")

    def check_ball_padding_collision(self, paddle_a_ycor, paddle_b_ycor):
        if (self.xcor() < -340 and self.xcor() > -350) and (
            self.ycor() < paddle_a_ycor + 30 and self.ycor() > paddle_a_ycor - 30
        ):
            self.setx(-340)
            self.dx *= -1
            os.system("aplay bounce.wav&")

        if (self.xcor() > 340 and self.xcor() < 350) and (
            self.ycor() < paddle_b_ycor + 30 and self.ycor() > paddle_b_ycor - 30
        ):
            self.setx(340)
            self.dx *= -1
            os.system("aplay bounce.wav&")


class Pen(Turtle):
    def __init__(self, color):
        Turtle.__init__(self)
        self.speed(0)
        self.color(color)
        self.penup()
        self.hideturtle()
        self.goto(0, 260)

    def write_ball_position(self, ball_x, ball_y):
        self.clear()
        self.write(
            f"Ball X:{ball_x}, Ball Y:{ball_y}",
            align="center",
            font=("Courier", 12, "normal"),
        )
    
    def write_paddle_position(self, paddle_a_y, paddle_b_y):
        self.clear()
        self.write(
            f"PaddleA Y:{paddle_a_y}, PaddleA Y:{paddle_b_y}",
            align="center",
            font=("Courier", 12, "normal"),
        )

    def write_score_board(self, player_a_score, player_b_score):
        self.clear()
        self.write(f"Player A: {player_a_score} | Player B: {player_b_score}",align="center", font=("Courier", 12, "normal"))


class Pong(object):
    def __init__(self, title, bgcolor):
        self.wn = Screen()
        self.wn.title(f"{title}")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)

    def main(self):
        self.wn.update()

    def move_paddle(self, move, key):
        self.wn.listen()
        self.wn.onkey(move, key)


def launch_game():
    # Initialize objects
    paddle_a = Paddle("square", "white", (-350, 0))
    paddle_b = Paddle("square", "red", (350, 0))
    ball = Ball("circle", "white")
    pen = Pen("white")
    game = Pong("Pong by @waltzfordebby", "black")

    # Event Listener
    game.move_paddle(paddle_a.move_up, "w")
    game.move_paddle(paddle_a.move_down, "s")
    game.move_paddle(paddle_b.move_up, "Up")
    game.move_paddle(paddle_b.move_down, "Down")

    while True:
        game.main()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        
        # Write board
        # pen.write_ball_position(ball.xcor(), ball.ycor())
        # pen.write_paddle_position(paddle_a.ycor(), paddle_b.ycor())
        pen.write_score_board(paddle_a.score, paddle_b.score)

        # Border checking
        ball.check_border_collision(paddle_a, paddle_b)

        # Paddle and ball collisions
        ball.check_ball_padding_collision(paddle_a.ycor(), paddle_b.ycor())


if __name__ == "__main__":
    launch_game()
