from turtle import Screen
import time
from Snake import Snake
from food import Food
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

score = 0
snake = Snake()
food = Food()
scoreboard = Scoreboard()

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_scoreboard()
        snake.create_snake()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_on = False
            scoreboard.game_over()

screen.exitonclick()

# random_position = (randint(0, 280), randint(0, 280))
# snakeFood = Turtle("circle")
# snakeFood.color("blue")
# snakeFood.shapesize(0.7, 0.7, 0.1)
# snakeFood.penup()
# snakeFood.setposition(random_position)
