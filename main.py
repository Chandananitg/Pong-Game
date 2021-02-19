from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)

screen.bgcolor("chartreuse4")
screen.title("Ping Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
game_is_on = True


def stop():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkey(stop, "space")


def reset():
    global wait_time
    ball.reset_ball()
    l_paddle.reset_paddle(-350)
    r_paddle.reset_paddle(350)
    scoreboard.reset_score()
    wait_time = 0.09


wait_time = 0.05
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(wait_time)
    if ball.ycor() >= 289 or ball.ycor() <= -280:
        ball.wall_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()
        wait_time = wait_time * 0.9
    elif abs(ball.xcor()) > 390:
        time.sleep(1)
        if ball.xcor() > 390:
            scoreboard.l_scoreup()
        if ball.xcor() < -390:
            scoreboard.r_scoreup()
        reset()
        screen.update()
        time.sleep(1)

screen.exitonclick()
