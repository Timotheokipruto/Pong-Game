from turtle import Turtle


class Paddle(Turtle):


    def __init__(self,coordinates) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(coordinates)


    def go_up(self):
        '''
        Goes up
        '''
        y_pos = self.ycor()+20
        self.goto(self.xcor(),y_pos)

    def go_down(self):
        y_pos = self.ycor()-20
        self.goto(self.xcor(),y_pos)

