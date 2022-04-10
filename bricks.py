from turtle import Turtle

start_x = [-360 + 90 * i for i in range(10)]
COLORS = ["Red", "orange", "yellow", "green", "blue", "violet"]


class Bricks(Turtle):
    def __init__(self):
        self.all_bricks = []
        super().__init__()
        self.create_brick()

    def create_brick(self):
        for i in range(48):
            brick = Turtle("square")
            brick.color("white")
            brick.shapesize(1, 4)
            brick.penup()
            if i < 10:
                brick.goto(start_x[i] - 40, 250)
                brick.color(COLORS[0])
            elif 19 > i > 9:
                i -= 10
                brick.goto(start_x[i], 220)
                brick.color(COLORS[1])
            elif 29 > i > 18:
                i -= 19
                brick.goto(start_x[i] - 40, 190)
                brick.color(COLORS[2])
            elif 38 > i > 28:
                i -= 29
                brick.goto(start_x[i], 160)
                brick.color(COLORS[3])
            elif 48 > i > 37:
                i -= 38
                brick.goto(start_x[i] - 40, 130)
                brick.color(COLORS[4])
            self.all_bricks.append(brick)
