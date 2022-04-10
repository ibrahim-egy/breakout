import time
from turtle import Screen
from player import Player
from bricks import Bricks
from ball import Ball

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Create objects
mo2a = Player()
bricks = Bricks()
ball = Ball()

# Wait for events
screen.listen()
screen.onkeypress(fun=mo2a.left, key="Left")
screen.onkeypress(fun=mo2a.right, key="Right")

game_is_on = True
sleep_time = 0.05
while game_is_on:
    ball.move()
    time.sleep(sleep_time)
    screen.update()

    if ball.ycor() < -280:
        game_is_on = False
        ball.home()
        ball.write("GAME OVER", move=False, align="center", font=("Ariel", 25, 'normal'))
    if ball.ycor() > 280 or ball.distance(mo2a) < 30:
        ball.bounce_y()
    if ball.xcor() > 430 or ball.xcor() < -430:
        ball.bounce_x()

    for brick in bricks.all_bricks:
        if brick.distance(ball) < 30:
            ball.bounce_y()
            brick.reset()

screen.exitonclick()
