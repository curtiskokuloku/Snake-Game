import turtle
import random


class Food:
    """
    Food class to represent the food in the game.
    """

    def __init__(self):
        """
        Initialize the food at a random position.
        """
        # Initialize the x and y coordinates of the food.
        self.x = 0
        self.y = 0

        # Set the color of the food pellet to red.
        self.color = "red"

        # Create a new turtle object to represent the food pellet.
        self.food = turtle.Turtle()

        # Set the speed of the turtle to the fastest speed for immediate display.
        self.food.speed(0)

        # Set the fill color of the turtle to the specified color.
        self.food.fillcolor(self.color)

        # Begin filling the turtle shape.
        self.food.begin_fill()

        # Set the shape of the turtle to a circle and adjust its size.
        self.food.shape("circle")
        self.food.shapesize(1.5, 1.5)

        # End filling the turtle shape.
        self.food.end_fill()

        # Lift up the turtle's pen to prevent drawing lines when moving.
        self.food.penup()

        # Set a random position for the food pellet on the grid.
        self.random_position()

    def random_position(self):
        """
        Set a random position for the food pellet within the grid boundaries.
        """
        # Calculate random x and y coordinates for the food pellet based on the grid size.
        self.x = 15 + 30 * random.randint(0, 19)
        self.y = 15 + 30 * random.randint(0, 19)

        # Set the position of the food pellet turtle to the random coordinates.
        self.food.setpos(self.x, self.y)
