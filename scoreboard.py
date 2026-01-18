FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("black")

    def increase_score(self):
        self.score += 1

    def refresh_board(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over Score: {self.score}", False, align="center", font=FONT)