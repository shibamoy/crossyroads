from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1

    def game_over(self):
        end_game = Turtle()
        end_game.color("black")
        end_game.hideturtle()
        end_game.penup()
        end_game.write(f"Game Over. Final Level: {self.level}",False ,align='center', font=('Arial', 10, 'normal'))

    def live_score(self):
        current_score = Turtle()
        current_score.penup()
        current_score.hideturtle()
        current_score.color("black")
        current_score.goto(-270,280)
        current_score.write(f"Level: {self.level}",False ,align='center', font=('Arial', 10, 'normal'))

