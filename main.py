import time
import random
from turtle import Turtle, Screen


class TurtleRace:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=960, height=467)
        self.screen.title("Turtle Race")
        self.screen.bgpic("track.png")
        self.screen.tracer(0)

        self.colors = ["red", "orange", "green", "blue", "purple"]
        self.turtles = []

        self.race()

    def racers(self):
        chosen_colors = random.sample(self.colors, 5)
        y_axis = -178

        for color in chosen_colors:
            turtle = Turtle("turtle")
            turtle.color(color)
            turtle.shapesize(2.3)
            turtle.speed(0)
            turtle.penup()
            turtle.goto(-450, y_axis)
            self.turtles.append(turtle)
            y_axis += 89
            self.screen.update()

    def race(self):
        self.racers()

        user_turtle = ""

        while user_turtle.lower() not in self.colors:
            user_turtle = self.screen.textinput(title="Choose your Turtle", prompt="Blue, Green, Orange, Purple, Red")

        on_game = True
        while on_game:
            self.screen.tracer(1)

            for turtle in self.turtles:
                turtle_distance = random.randint(6, 12)
                turtle.forward(turtle_distance)
                if turtle.xcor() >= 400:
                    winner = turtle.pencolor()
                    score_turtle = Turtle()
                    score_turtle.hideturtle()
                    score_turtle.speed(0)
                    score_turtle.penup()
                    score_turtle.color(winner)
                    if winner == user_turtle:
                        score_turtle.goto((turtle.xcor() - 30), (turtle.ycor() - 15))
                        score_turtle.write(f"You Won 🎉", font=("Courier", 28, "bold"), align="right")
                    else:
                        score_turtle.goto((turtle.xcor() - 30), (turtle.ycor() - 15))
                        score_turtle.write(f"you lost! {winner.capitalize()} is the Winner",
                                           font=("Courier", 28, "bold"), align="right")
                    on_game = False
                    break
        self.play_again()

    def play_again(self):
        time.sleep(2)
        self.screen.clear()
        self.screen.bgpic("track.png")
        self.screen.tracer(0)
        self.screen.update()
        self.race()


if __name__ == '__main__':
    TurtleRace()
