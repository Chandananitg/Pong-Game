from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.reset_score()

    def l_scoreup(self):
        self.l_score += 1

    def r_scoreup(self):
        self.r_score += 1

    def reset_score(self):
        self.clear()
        self.draw_midline()
        self.setposition(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.setposition(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def draw_midline(self):
        self.setposition(0, 300)
        self.setheading(270)
        self.pendown()
        self.pencolor("white")
        self.pensize(3)
        for _ in range(60):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.penup()
        self.draw_circle()
        self.draw_border()

    def draw_circle(self):
        radius1 = 100
        radius2 = 270

        self.goto(240,0)
        self.pendown()
        self.circle(radius2)
        self.penup()

        self.setheading(90)
        self.goto(-260,0)
        self.pendown()
        self.circle(radius2)
        self.penup()

        self.goto(0,-radius1)
        self.pendown()
        self.setheading(0)
        self.circle(radius1)
        self.penup()

    def draw_border(self):
        self.penup()
        self.goto(-397.5,-290)
        self.setheading(90)
        self.pendown()
        self.pencolor("black")
        for _ in range(2):
            self.forward(587.5)
            self.right(90)
            self.forward(787.5)
            self.right(90)
        self.penup()
        self.color("white")

