from turtle import Turtle

STARTING_POSITION = (0, -250)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.color("white")
        self.shape("square")
        self.shapesize(0.5, 5)

    def left(self):
        self.setx(self.xcor() - 20)

    def right(self):
        self.setx(self.xcor() + 20)
