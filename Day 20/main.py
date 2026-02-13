from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.25)
    snake.move()

    #Detect collision with food
    if snake.squares[0].distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()

    #Detect collision with wall
    if snake.squares[0].xcor() > 290 or snake.squares[0].xcor() < -290 or snake.squares[0].ycor() > 290 or snake.squares[0].ycor() < -290:
        game_is_on = False
        score.game_over()

    #detect collision with tail
    for square in snake.squares[1:]:
        if snake.squares[0].distance(square) < 15:
            game_is_on = False
            score.game_over()

screen.exitonclick()