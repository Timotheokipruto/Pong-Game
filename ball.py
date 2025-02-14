from turtle import Turtle

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()

        self.shape("circle")
        self.width(20)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        

    def move(self): 
        x_pos = self.xcor()+self.x_move
        y_pos = self.ycor()+self.y_move
        self.goto(x_pos,y_pos)

    
    def bounce_y(self):
        self.y_move*=-1


    def bounce_x(self):
        self.x_move*=-1
        self.move_speed*=0.9

    def reset_pos(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()


    
