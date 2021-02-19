from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=2.5)
        self.color("black", "white")
        self.penup()
        self.setposition(coor)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def reset_paddle(self, rcor):
        self.goto(rcor, 0)
