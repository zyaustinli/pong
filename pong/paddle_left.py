from turtle import Turtle

class Paddle_left(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(6, 0.5)
        self.color("white")
        self.goto(-280,0)


        self.speed("fastest")

    def up(self):
        if self.ycor()<240:

            self.goto(self.xcor(), self.ycor()+25)

    def down(self):
        if self.ycor()>-240:
            self.goto(self.xcor(), self.ycor()-25)