
import turtle
import random


class Game:
    """
    Purpose:
        represents the entities that need to be manipulated for thr game; it draws the board and call a bunch of turtle
        functions that ensure that the turtle graphics are running as fast as possible.
    Instance variables:
        self.player - represents a Snake object
        self.food- represents a Food object
        self.player.user_score - calls the score of the player
        self.gameloop - calls the gameloop method
        self.is_game_over - boolean that determines whether the game is over or not
        self.game_over - turtle object hat displays 'Game over' when the snake collides with the boundary or itself
    Methods:
        __init__ - constructor that ensure that the turtle graphics are running as fast as possible, listens for the key
        press, and creates objects of Snake and Food.
        gameloop - a function that calls itself at a set interval to keep the game moving.
        restart - takes in no argument other than self amd restarts the game when 'r' key is pressed.
    """

    def __init__(self):
        self.is_game_over = False
        turtle.setup(700, 700)  # Setup 700x700 pixel window
        turtle.setworldcoordinates(-40, -40, 640, 640)  # Bottom left of screen is (-40, -40), top right is (640, 640)
        cv = turtle.getcanvas()
        cv.adjustScrolls()
        turtle.hideturtle()  # Ensure turtle is running as fast as possible
        turtle.delay(0)
        turtle.tracer(0, 0)
        turtle.speed(0)
        for i in range(4):  # Draw the board as a square from (0,0) to (600,600)
            turtle.forward(600)
            turtle.left(90)
        turtle.title('Snake Game made by Curtis K')
        turtle.bgcolor('beige')
        self.game_over = turtle.Turtle()
        self.game_over.hideturtle()
        self.player = Snake(315, 315, 'green')
        self.food = Food()
        self.player.user_score()
        self.gameloop()
        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.onkeypress(self.player.go_right, 'Right')
        turtle.onkeypress(self.player.go_left, 'Left')
        turtle.onkeypress(self.restart, 'r')
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
        self.player.move(self.food)
        if not self.player.body_collision() and not self.player.boundary_collision():
            turtle.ontimer(self.gameloop, 200)
            turtle.update()
        else:
            self.player.current_score = 0
            self.player.score.clear()
            self.player.user_score()
            self.game_over.penup()
            self.game_over.setpos(315, 315)
            self.game_over.write("Game Over", True, align="center", font=('Arial', 20, 'normal'))
            self.is_game_over = True

    def restart(self):
        self.player.restart()
        self.player.x = 315
        self.player.y = 315
        self.player.vx = 0
        self.player.vy = 0
        self.player.grow()
        self.food.random_position()
        if self.is_game_over:
            self.game_over.clear()
            self.is_game_over = False
            self.gameloop()


class Snake:
    """
    Purpose:
        represents one of the snakes involved in the game. In my version, there will be only one snake.
    Instance variables:
        self.x, self.y - integers representing the current position of the snake
        self.vx, self.vy - integers representing the snake's current velocity
        self.color - represents the color of the snake
        self.current_score - represents the current score of the player
        self.high_score - represents the player's high score
        self.segments - list that stores the square segments that make up the snake
        self.grow - calls the grow(self) method
        self.score - turtle object that displays the player's score
    Methods:
        __init__ - constructor that takes in three arguments aside from self that represents the snake's position,
        color, and segments.
        user_score - displays the player's score on the turtle screen
        grow - creates a new head segment for the snake at the current position
        move - increases the snake's x-position by 30 and then moves the head of the snake to the updated position
        go_down, go_up, go_left, go_right - change the position of the snake's head by either -30, 0, or 30
        boundary_collision - checks if the snake's head goes beyond the walls/boundaries
        body_collision - checks if the snake collides with any of the other segments
        restart - clears all the snake's object in segments and add a new one - the head - and sets the score to 0
    """

    def __init__(self, x, y, color):
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
        self.score = turtle.Turtle()
        self.score.speed(0)
        self.score.shape("square")
        self.score.color("black")
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(315, 610)
        self.score.write("Score: {} High Score: {}".format(self.current_score, self.high_score), align="center",
                         font=("Courier", 24, "normal"))

    def grow(self):
        head = turtle.Turtle()
        head.speed(0)
        head.fillcolor(self.color)
        head.begin_fill()
        head.shape('square')
        head.shapesize(1.5, 1.5)
        head.end_fill()
        head.penup()
        head.setpos(self.x, self.y)
        self.segments.append(head)

    def restart(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.current_score = 0
        self.score.clear()
        self.user_score()

    def move(self, food):
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
        self.vx = 0
        self.vy = -30

    def go_up(self):
        self.vx = 0
        self.vy = 30

    def go_right(self):
        self.vx = 30
        self.vy = 0

    def go_left(self):
        self.vx = -30
        self.vy = 0

    def boundary_collision(self):
        return self.x <= 0 or self.x >= 600 or self.y >= 600 or self.y <= 0

    def body_collision(self):
        for s in range(len(self.segments) - 1):
            if self.x == self.segments[s].xcor() and self.y == self.segments[s].ycor():
                return True
        return False


class Food:
    """
    Purpose:
        represents the food pellet that is placed in a random position aligned with the grid
    Instance variables:
        self.x, self.y = represents the position of the food
        self.color - represents the color of the food
        self.food - represents the turtle object that creates the food
        self.random_position - calls the random_position method to pick a random position for the food
    Methods:
        __init__ takes in no argument other than self, and initialize the position, color, and shape of the food object
        random_position - chooses a random x and y coordinates of the food pellet every time the snake 'eats' it
    """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = 'red'
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.fillcolor(self.color)
        self.food.begin_fill()
        self.food.shape('circle')
        self.food.shapesize(1.5, 1.5)
        self.food.end_fill()
        self.food.penup()
        self.random_position()

    def random_position(self):
        self.x = 15 + 30 * random.randint(0, 19)
        self.y = 15 + 30 * random.randint(0, 19)
        self.food.setpos(self.x, self.y)


Game()
