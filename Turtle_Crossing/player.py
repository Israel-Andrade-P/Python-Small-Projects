from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.create_turtle()


    def create_turtle(self):
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.reset_pos()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y    

    def reset_pos(self):
        self.goto(STARTING_POSITION)                

