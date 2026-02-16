import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# ----- Screen setup -----
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)   # Turn off auto animation for manual frame updates
screen.listen()

# ----- Game objects -----
scoreboard = Scoreboard()
player = Player()
cars = CarManager()

# Control: player moves up with arrow key
screen.onkeypress(player.move, "Up")

# ----- Game loop -----
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()   # Possibly spawn a new car
    cars.move()         # Move all existing cars

    # If player reaches finish line → level up
    if player.ycor() > 290:
        player.restart()
        cars.increase_speed()
        scoreboard.add_lvl()

    # Detect collision with any car
    for car in cars.list_of_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

# Keep window open after game ends
screen.exitonclick()
