from turtle import Screen
from player import Player
from cars import Cars
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()

player = Player((0, -280))


screen.onkey(player.player_move,"w")

cars = Cars()


collide = False
game_on = True

while game_on:

    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()
    for car in cars.all_cars:
        if player.distance(car) < 20:
            print("Collision")








screen.exitonclick()
