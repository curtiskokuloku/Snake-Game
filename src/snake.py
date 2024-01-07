import turtle


class Snake:
    """
    Represents the snake entity in the game.

    Attributes:
        x (int): Current x-coordinate of the snake.
        y (int): Current y-coordinate of the snake.
        vx (int): Velocity in x-direction.
        vy (int): Velocity in y-direction.
        color (str): Color of the snake.
        current_score (int): Current score of the player.
        high_score (int): Highest score achieved by the player.
        segments (list): List to store the segments of the snake.
        score (turtle.Turtle): Turtle object to display the score on the screen.
    """

    def __init__(self, x, y, color):
        """
        Initialize the snake with position, color, and other attributes.

        Args:
            x (int): Initial x-coordinate.
            y (int): Initial y-coordinate.
            color (str): Color of the snake.
        """
        self.x = x
        self.vx = 0
        self.y = y
        self.vy = 0
        self.color = color
        self.current_score = 0
        self.high_score = 0
        self.segments = []
        self.grow()
        self.score = None

    def user_score(self):
        """
        Display the player's score on the screen using turtle graphics.
        """
        # Create a new turtle object to display the score.
        self.score = turtle.Turtle()

        # Set the speed of the turtle to the fastest speed for immediate display.
        self.score.speed(0)

        # Set the shape of the turtle to a square for simplicity.
        self.score.shape("square")

        # Set the color of the turtle to black for readability.
        self.score.color("black")

        # Lift up the turtle's pen to prevent drawing lines when moving.
        self.score.penup()

        # Hide the turtle to only display the text without seeing the turtle itself.
        self.score.hideturtle()

        # Set the position of the turtle to the desired location on the screen.
        self.score.goto(315, 610)

        # Write the current score and high score on the screen.
        self.score.write(
            "Score: {} High Score: {}".format(self.current_score, self.high_score),
            align="center",
            font=("Courier", 24, "normal"),
        )

    def grow(self):
        """
        Add a new segment to the snake representing its growth.
        """
        # Create a new turtle object to represent the new segment of the snake.
        head = turtle.Turtle()

        # Set the speed of the turtle to the fastest speed.
        head.speed(0)

        # Set the fill color of the turtle to the snake's color.
        head.fillcolor(self.color)

        # Begin the filling of the turtle shape.
        head.begin_fill()

        # Set the shape of the turtle to a square and adjust its size.
        head.shape("square")
        head.shapesize(1.5, 1.5)

        # End the filling of the turtle shape.
        head.end_fill()

        # Lift up the turtle's pen to prevent drawing lines when moving.
        head.penup()

        # Set the position of the new segment to the snake's current position.
        head.setpos(self.x, self.y)

        # Add the new segment (turtle object) to the segments list of the snake.
        self.segments.append(head)

    def restart(self):
        """
        Reset the snake to its initial state.
        """
        # Hide each segment of the snake from the screen.
        for seg in self.segments:
            seg.hideturtle()

        self.segments.clear()  # Clear the segments list to remove all previous segments from memory.
        self.current_score = 0  # Reset the current score to zero.
        self.score.clear()  # Clear the previous score displayed on the screen.
        self.user_score()  # Update the score display to reflect the reset score.

    def move(self, food):
        """
        Move the snake and handle collisions with the food.

        Args:
            food (Food): Food object to check for collisions and update the score.
        """
        # Update the snake's x and y coordinates based on its velocity.
        self.x += self.vx
        self.y += self.vy

        # Check if the snake's head coordinates match the food coordinates.
        if self.x == food.x and self.y == food.y:
            # If there's a collision with food, grow the snake, update food position,
            # increase the score, and update the displayed score.
            self.grow()
            food.random_position()
            self.current_score += 10

            # Update the high score if the current score surpasses it.
            if self.current_score > self.high_score:
                self.high_score = self.current_score

            # Clear the previous score display and update with the new score.
            self.score.clear()
            self.user_score()
        else:
            # If the snake doesn't collide with food, move each segment of the snake forward.
            for i in range(len(self.segments) - 1):
                # Move each segment to the position of the segment in front of it.
                self.segments[i].setx(self.segments[i + 1].xcor())
                self.segments[i].sety(self.segments[i + 1].ycor())

            # Update the position of the snake's head to its new position.
            head = self.segments[-1]
            head.setpos(self.x, self.y)

    def go_down(self):
        """
        Set the snake's direction to move downwards.
        """
        self.vx = 0
        self.vy = -30

    def go_up(self):
        """
        Set the snake's direction to move upwards.
        """
        self.vx = 0
        self.vy = 30

    def go_right(self):
        """
        Set the snake's direction to move rightwards.
        """
        self.vx = 30
        self.vy = 0

    def go_left(self):
        """
        Set the snake's direction to move leftwards.
        """
        self.vx = -30
        self.vy = 0

    def boundary_collision(self):
        """
        Check if the snake has collided with the boundaries.

        Returns:
            bool: True if collision occurs, False otherwise.
        """
        return self.x <= 0 or self.x >= 600 or self.y >= 600 or self.y <= 0

    def body_collision(self):
        """
        Check if the snake has collided with its own body.

        Returns:
            bool: True if collision occurs, False otherwise.
        """
        for s in range(len(self.segments) - 1):
            if self.x == self.segments[s].xcor() and self.y == self.segments[s].ycor():
                return True
        return False
