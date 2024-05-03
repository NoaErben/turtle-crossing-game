from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.setposition(-220,260)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg= f"Level: {self.level}", align= "center", font= FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write(arg= "GAME OVER", align= "center", font=FONT)

    def add_point(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()



