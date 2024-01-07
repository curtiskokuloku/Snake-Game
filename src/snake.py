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
        self.score = turtle.Turtle()
        self.score.speed(0)
        self.score.shape("square")
        self.score.color("black")
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(315, 610)
        self.score.write(
            "Score: {} High Score: {}".format(self.current_score, self.high_score),
            align="center",
            font=("Courier", 24, "normal"),
        )

    def grow(self):
        """
        Add a new segment to the snake representing its growth.
        """
        head = turtle.Turtle()
        head.speed(0)
        head.fillcolor(self.color)
        head.begin_fill()
        head.shape("square")
        head.shapesize(1.5, 1.5)
        head.end_fill()
        head.penup()
        head.setpos(self.x, self.y)
        self.segments.append(head)

    def restart(self):
        """
        Reset the snake to its initial state.
        """
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.current_score = 0
        self.score.clear()
        self.user_score()

    def move(self, food):
        """
        Move the snake and handle collisions with the food.

        Args:
            food (Food): Food object to check for collisions and update the score.
        """
        self.x += self.vx
        self.y += self.vy
        if self.x == food.x and self.y == food.y:
            self.grow()
            food.random_position()
            self.current_score += 10
            if self.current_score > self.high_score:
                self.high_score = self.current_score
            self.score.clear()
            self.user_score()
        else:
            for i in range(len(self.segments) - 1):
                self.segments[i].setx(self.segments[i + 1].xcor())
                self.segments[i].sety(self.segments[i + 1].ycor())
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
