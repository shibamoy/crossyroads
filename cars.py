from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "blue", "purple", "green"]
MOVE_INCREMENT = 10
STARTING_MOVE_DISTANCE = 5

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []


    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for cars in self.all_cars:
            self.penup()
            x = cars.xcor()
            x -= 10
            cars.setx(x)


