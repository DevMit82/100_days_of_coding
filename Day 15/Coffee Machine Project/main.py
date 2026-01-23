MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink):
    if drink == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            return False
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            return False
    elif drink == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            return False
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            return False
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False

    elif drink == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            return False
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            return False
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False

    return True


turn_off = False
check = False
money = 0

while not turn_off:
    # TODO ask user for input
    user_select = input("What would you like? (espresso/latte/cappuccino) ").lower()
    # TODO check user input
    # user can choose "off", "report" or a drink
    # TODO turn off the coffee machine
    if user_select == "off":
        turn_off = True
    elif user_select == "report":
        # TODO print resources line bye line
        for key, value in resources.items():
            print(f"{key}: {value}")
        print(f"money: ${money}")
        continue
    # TODO check resources
    elif user_select == "espresso":
        check = check_resources("espresso")
    elif user_select == "latte":
        check = check_resources("latte")
    elif user_select == "cappuccino":
        check = check_resources("cappuccino")
    else:
        print("Choice not exists. Please try again!")
        continue

    if check is True:
        print("Please insert coins!")
        quarters = float(input("how many quarters? "))
        dimes = float(input("how many dimes? "))
        nickels = float(input("how many nickles? "))
        pennies = float(input("how many pennies? "))
        # TODO calculate coins
        inserted_coins = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

        if user_select == "espresso" and inserted_coins >= MENU["espresso"]["cost"]:
            # calculate change
            change = inserted_coins - MENU["espresso"]["cost"]
            # update resources
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        elif user_select == "latte" and inserted_coins >= MENU["latte"]["cost"]:
            # calculate change
            change = inserted_coins - MENU["latte"]["cost"]
            # update resources
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        elif user_select == "cappuccino" and inserted_coins >= MENU["cappuccino"]["cost"]:
            # calculate change
            change = inserted_coins - MENU["cappuccino"]["cost"]
            # update resources
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]

            # give back money and ask again
        else:
            inserted_coins -= inserted_coins
            print("Sorry that's not enough money. Money refunded.")
            continue

        # TODO update money
        money = inserted_coins - change
        # TODO tell user to take product
        print(f"Here is ${change:.2f} in change")
        print(f"Here is your {user_select}. Enjoy!")
