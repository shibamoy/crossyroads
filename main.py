from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()
#change back to starting position later
player = Player((0, -280))
cars = Cars()
score = Score()
#reset screen
def refresh(fast):
    screen.clear()
    screen.tracer(0)
    time.sleep(fast)
    screen.update()

collide = False
game_on = True
speed = 0.1
while game_on:

    screen.onkey(player.player_move, "w")
    time.sleep(speed)
    screen.update()
    score.live_score()
    cars.create_car()
    cars.move()
    #checks for collision
    for car in cars.all_cars:
        if player.distance(car) < 22:
            print("Collision")
            collide = True
            if collide:
                #prints final score and game over
                score.game_over()
                collide = False
                game_on = False
    if player.ycor() > 250:
        score.level += 1
        speed *= 0.8
        print(speed)
        refresh(speed)
        player = Player((0, -280))

















screen.exitonclick()
