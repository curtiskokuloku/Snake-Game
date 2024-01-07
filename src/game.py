import turtle
from snake import Snake
from food import Food
import random


class Game:
    """
    Represents the main game environment and controls the game's logic and flow.
    """

    def __init__(self):
        """
        Initialize the game and its components.
        """
        # Initialize turtle screen settings
        self.setup_screen()

        # Create game components
        self.player = Snake(315, 315, "green")
        self.food = Food()

        # Display the user's score on the screen.
        self.player.user_score()

        # Start the game loop
        self.game_loop()

        # Set up key bindings
        self.setup_key_bindings()

        # Enable listening for keypress events.
        turtle.listen()

        # Start the turtle main event loop.
        turtle.mainloop()

    def setup_screen(self):
        """
        Set up the turtle screen settings.
        """
        # Initialize the game over state to False.
        self.is_game_over = False

        # Set up the turtle graphics window with specific dimensions and coordinates.
        turtle.setup(700, 700)
        turtle.setworldcoordinates(-40, -40, 640, 640)

        # Adjust the canvas and set turtle configurations for optimal performance.
        cv = turtle.getcanvas()
        cv.adjustScrolls()
        turtle.hideturtle()
        turtle.delay(0)
        turtle.tracer(0, 0)
        turtle.speed(0)

        # Draw the game board as a square from (0,0) to (600,600).
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)

        # Set the title and background color for the game window.
        turtle.title("Snake Game made by Curtis K")
        turtle.bgcolor("beige")

        # Create the game over turtle object and hide it initially.
        self.game_over = turtle.Turtle()
        self.game_over.hideturtle()

    def game_loop(self):
        """
        Main game loop that updates the game state.
        """
        # Move the snake based on user input and update the game state.
        self.player.move(self.food)

        # Check for collisions with the snake's body or game boundaries.
        if not self.player.body_collision() and not self.player.boundary_collision():
            # If no collisions, continue the game loop with a delay of 200 milliseconds.
            turtle.ontimer(self.game_loop, 200)
            turtle.update()
        else:
            # If collision occurs, display game over message and set game over state to True.
            self.player.current_score = 0
            self.player.score.clear()
            self.player.user_score()
            self.game_over.penup()
            self.game_over.setpos(315, 315)
            self.game_over.write(
                "Game Over", True, align="center", font=("Arial", 20, "normal")
            )
            self.is_game_over = True

    def restart(self):
        """
        Restart the game by resetting the snake and food positions and clearing the game over message.
        """

        # Reset the snake's position and attributes.
        self.player.restart()
        self.player.x = 315
        self.player.y = 315
        self.player.vx = 0
        self.player.vy = 0
        self.player.grow()

        # Randomly position the food pellet on the grid.
        self.food.random_position()

        # If the game over state is True, clear the game over message and restart the game loop.
        if self.is_game_over:
            self.game_over.clear()
            self.is_game_over = False
            self.game_loop()

    def setup_key_bindings(self):
        """
        Set up key bindings for controlling the snake.
        """
        # Set up keypress event listeners for snake movement and game restart.
        turtle.onkeypress(self.player.go_down, "Down")
        turtle.onkeypress(self.player.go_up, "Up")
        turtle.onkeypress(self.player.go_right, "Right")
        turtle.onkeypress(self.player.go_left, "Left")
        turtle.onkeypress(self.restart, "r")
