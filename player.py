from turtle import Turtle
STARTING_POSITION = (0,-250)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 200

class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(position)
        self.seth(90)

    def player_move(self):
        self.forward(10)


