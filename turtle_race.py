from turtle import Turtle, Screen
from random import choice, randint


def make_turtles():
    turtles = []
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
    position_x = -240
    position_y = [-150, -100, -50, 0, 50, 100, 150]
    
    for index in range(7):
        turtle = Turtle("turtle")
        turtle.penup()
        turtle.color(colors[index])
        turtle.goto(position_x, position_y[index])
        turtles.append(turtle)

    return turtles    

def start_race(turtles, u_bet):
    is_race_on = True
    while is_race_on:

        for turtle in turtles:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                if u_bet == winning_color:
                    print(f"You've won! The {winning_color} turle is the winner!")
                    
                else:
                    print(f"You've lost! The {winning_color} turle is the winner!")

                is_race_on = False    
                break    


            rand_distance = randint(0, 10)
            turtle.forward(rand_distance)


screen = Screen()
screen.setup(width=500, height=400)
        
racers = make_turtles()

user_bet = screen.textinput(title="Make your bet", prompt="Which turle wil win the race? Enter a color: ")

start_race(racers, user_bet)

screen.exitonclick()