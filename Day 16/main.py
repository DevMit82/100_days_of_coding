from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of each class
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

# Flag to control whether the machine is runnin
is_on = True
# Main program loop
while is_on:
    # Ask the user for their choice and show available menu items
    user_select = input(f"What would you like? ({my_menu.get_items()}) ")
    # Turn off the machine
    if user_select == "off":
        is_on = False
    # Print a report of current resources
    elif user_select == "report":
        my_coffee_maker.report()
    else:
        # Handle drink selectio
        drink = my_menu.find_drink(user_select)
        # Check if resources are sufficient AND payment is successful
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            # If both checks pass, make the coffee
            my_coffee_maker.make_coffee(drink)








