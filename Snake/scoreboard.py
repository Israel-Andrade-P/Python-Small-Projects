from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.setpos(0, 265)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGMENT, font=FONT)    

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over_text(self):
        self.setpos(0, 0)
        self.write("GAME OVER", move=False, align=ALIGMENT, font=FONT)    
        
        