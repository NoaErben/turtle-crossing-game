from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1,2)
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.setposition(x= random.randint(-370,300), y=random.randint(-250, 250))
        self.move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.move_distance)

    def add_more_cars(self):
        self.setposition(x= random.randint(320,360), y= random.randint(-230,230))

    def increase_the_distance(self):
        self.move_distance += MOVE_INCREMENT
        


