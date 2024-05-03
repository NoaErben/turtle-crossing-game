import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.listen()
screen.title("The player crossing game")
screen.tracer(0)

player = Player()
screen.onkey(key="Up", fun=player.move_up)

cars_list = []

for _ in range(10):
    car = CarManager()
    cars_list.append(car)

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    for car in cars_list:
        car.move()
        if car.xcor() < -320 :
            car.add_more_cars()
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
        if player.ycor() > 280:
            player.level_up()
            scoreboard.add_point()
            for car in cars_list:
                car.increase_the_distance()

    screen.update()



screen.exitonclick()
