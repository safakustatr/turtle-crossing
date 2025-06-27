import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    if player.ycor() > player.finish_line:
        scoreboard.level += 1
        scoreboard.refresh()
        player.refresh()
        car_manager.level_up()

    for car in car_manager.cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()