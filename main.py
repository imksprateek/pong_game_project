from turtle import Turtle, Screen
from paddle import Paddle_
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


r_paddle = Paddle_((350, 0))
l_paddle = Paddle_((-350, 0))
ball = Ball()
score1 = Scoreboard((100,200))
score2 = Scoreboard((-100,200))

screen.update()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    #Detect collision with the paddles
    if (ball.distance(r_paddle) <= 50 and ball.xcor() >= 340) or (ball.distance(l_paddle) <= 50 and ball.xcor() <= -340):
        ball.bounce_off_paddle()
        ball.speed_up()

    #Detect if the ball goes out of bounds
    if ball.xcor() >= 400:
        ball.reset_position()
        score2.increment()

    elif  ball.xcor() <= -400:
        ball.reset_position()
        score1.increment()



screen.exitonclick()