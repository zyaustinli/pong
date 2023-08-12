from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.update()
       

    def update(self):
        self.goto(-60,180)
        self.write(self.score_left, align="center", font=("Courier", 80, 'normal'))
        self.goto(60,180)
        self.write(self.score_right, align="center", font=("Courier", 80, 'normal'))



    def left_score(self):
        self.score_left+= 1
        self.clear()
        self.update()

    def right_score(self):
        self.score_right+= 1
        self.clear()
        self.update()

    