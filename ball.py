from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black","white")
        self.shapesize(outline=2)
        self.penup()
        self.x_direction = 10
        self.y_direction = 10

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def reset_ball(self):
        self.goto(0, 0)
        self.x_direction *= -1

    def wall_bounce(self):
        self.y_direction *= -1

    def paddle_bounce(self):
        self.x_direction *= -1
