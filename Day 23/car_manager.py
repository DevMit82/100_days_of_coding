from turtle import Turtle
import random

# Possible colors for cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# Initial movement speed of cars
STARTING_MOVE_DISTANCE = 5

# Speed increase applied when level goes up
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.list_of_cars = []            # Stores all active car objects
        self.ht()                         # Hide the manager turtle (not visible in game)
        self.car_speed = STARTING_MOVE_DISTANCE   # Current speed used for all cars

    def move(self):
        # Move every car forward using the current speed
        for car in self.list_of_cars:
            car.fd(self.car_speed)

    def increase_speed(self):
        # Increase global car speed (called when player levels up)
        self.car_speed += MOVE_INCREMENT

    def create_car(self):
        # Random chance each frame to spawn a new car (prevents overcrowding)
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            # Create a new car turtle
            new_car = Turtle("square")
            new_car.penup()                       # Prevent drawing while moving
            new_car.shapesize(stretch_len=2)      # Make car longer than tall
            new_car.seth(180)                     # Face left (towards player path)

            # Spawn on right edge at random vertical position
            new_car.goto(x=300, y=random.randint(-250, 250))

            # Assign a random color
            new_car.color(random.choice(COLORS))

            # Add new car to tracking list
            self.list_of_cars.append(new_car)
