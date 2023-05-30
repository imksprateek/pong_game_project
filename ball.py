from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.reset_speed()
        self.move_speed = 0.1

    def create_ball(self):
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(0,0)
    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)
    def bounce(self):
        self.y *= -1
    def bounce_off_paddle(self):
        self.x *= -1
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.x *= -1
        self.y *= -1
    def speed_up(self):
        self.move_speed *= 0.9
    def reset_speed(self):
        self.x = 10
        self.y = 10

