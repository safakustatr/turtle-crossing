from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "center"
POSITION = (-210, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.penup()
        self.goto(POSITION)
        self.hideturtle()
        self.color("black")
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)