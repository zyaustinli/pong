from turtle import Screen, Turtle
import time
from paddle_left import Paddle_left
from paddle_right import Paddle_right
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title('Pong')
screen.tracer(0)





paddle_left= Paddle_left()
paddle_right =Paddle_right()
ball = Ball()
scoreboard=  Scoreboard()



screen.listen()

screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")






game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)

    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 250 or ball.distance(paddle_left) < 50 and ball.xcor() < -250:
        ball.reflect()


    if ball.xcor()>300:
        ball.reset_position()
        scoreboard.left_score()
        #scoreleft += 1

    if ball.xcor()<-300:
        ball.reset_position()
        scoreboard.right_score()

        #scoreright += 1
        

screen.exitonclick()