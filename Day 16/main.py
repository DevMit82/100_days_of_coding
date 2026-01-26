from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()


is_on = True

while is_on:
    user_select = input(f"What would you like? ({my_menu.get_items()}) ")
    if user_select == "off":
        is_on = False
    elif user_select == "report":
        my_coffee_maker.report()
    else:
        drink = my_menu.find_drink(user_select)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)








