from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.finish_line = FINISH_LINE_Y
        self.penup()
        self.setheading(90)
        self.refresh()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        self.goto(STARTING_POSITION)