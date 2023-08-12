from turtle import Turtle

import random
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        
        self.goto(0,0)
        self.color("white")
        self.xcoor =10
        self.ycoor=15
        self.ball_speed = 0.1


    def move(self):
        self.goto(self.xcor()+self.xcoor, self.ycor()+self.ycoor)

    def reflect(self): #reflect off paddle
        self.xcoor *= -1
        self.ball_speed *= 0.9

    def bounce(self):
        self.ycoor *=-1

    def reset_position(self):
        self.ball_speed =0.1

        self.goto(0,0)
        self.reflect()
        if random.randint(1,2) == 1:
            self.bounce()