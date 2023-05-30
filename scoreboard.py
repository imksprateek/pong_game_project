from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Aerial", 60, "normal")

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.update_score()

    def increment(self):
        self.clear()
        self.score += 1
        self.update_score()

    def update_score(self):
        self.write(arg=f"{self.score}", font=FONT, align=ALIGNMENT)