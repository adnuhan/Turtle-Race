import time
import random
from turtle import Turtle, Screen


# Create a class to manage the turtle race
class TurtleRace:
    def __init__(self):
        # Set up the screen for the turtle race
        self.screen = Screen()
        self.screen.setup(width=960, height=467)
        self.screen.title("Turtle Race")
        self.screen.clear()
        self.screen.bgpic("track.png")
        self.screen.tracer(0)  # Turn off automatic screen updates for better performance

        # Start the race
        self.play()

    def play(self):

        # Define the available turtle colors
        colors = ["blue", "green", "orange", "purple", "red"]

        # Create a list to store the turtle objects
        turtles = []

        # Set the starting y-axis position for the turtles
        y_axis = -178

        # Create five turtles with different colors and positions
        for x in range(5):
            turtle = Turtle("turtle")
            turtle.color(colors[x])
            turtle.shapesize(2.3)
            turtle.speed(0)
            turtle.penup()
            turtle.goto(-450, y_axis)
            turtles.append(turtle)
            y_axis += 89
            self.screen.update()  # Update the screen to show the new turtle

        # Get user input for their chosen turtle color
        user_turtle = ""
        playing = ""

        try:
            # Give the user three attempts to choose a valid turtle color
            for i in range(3):
                user_turtle = self.screen.textinput(title="Choose your Turtle",
                                                    prompt="Blue, Green, Orange, Purple, Red")

                # Check if the input is a valid color
                if user_turtle.lower() in colors:
                    playing = True
                    break  # Exit the loop if a valid color is chosen

            # Start the race loop
            while playing:
                self.screen.tracer(1)  # Turn on automatic screen updates for the race

                # Randomly move each turtle
                for turtle in turtles:
                    turtle_distance = random.randint(7, 14)
                    turtle.forward(turtle_distance)

                    # Check if a turtle reaches the finish line
                    if turtle.xcor() >= 400:
                        winner = turtle.pencolor()  # Get the color of the winning turtle

                        # Create a turtle to display the winning message
                        score_turtle = Turtle()
                        score_turtle.hideturtle()
                        score_turtle.speed(0)
                        score_turtle.penup()
                        score_turtle.color(winner)

                        # Display win/lose message based on user's choice
                        if winner == user_turtle:
                            score_turtle.goto((turtle.xcor() - 30), (turtle.ycor() - 15))
                            score_turtle.write(f"You Won 🎉", font=("Courier", 28, "bold"), align="right")
                        else:
                            score_turtle.goto((turtle.xcor() - 30), (turtle.ycor() - 15))
                            score_turtle.write(f"you lost! {winner.capitalize()} is the Winner",
                                               font=("Courier", 28, "bold"), align="right")

                        # Stop the game loop and break out of the racer loop to end the race
                        playing = False
                        break

            time.sleep(2)  # Pause for 2 seconds after each round
            self.__init__()  # Restart the game after a short delay

        except AttributeError:  # Handle errors during user input (e.g., closing the window)
            print("Goodbye")


if __name__ == '__main__':
    TurtleRace()
