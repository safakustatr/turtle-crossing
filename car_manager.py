from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.cars = []
        self.generate_cars()

    def generate_cars(self):
        for _ in range(10):
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(random.randint(-270, 270), random.randint(-250, 270))
            new_car.move_distance = STARTING_MOVE_DISTANCE
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(car.move_distance)
            if car.xcor() < -300:
                car.goto(300, car.ycor())

    def level_up(self):
        for car in self.cars:
            car.move_distance += MOVE_INCREMENT