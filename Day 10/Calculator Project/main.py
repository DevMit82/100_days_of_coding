def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# result = operations["*"] (n1= 4, n2= 8)
# print(result)
#add logo from art.py
from art import logo


calc_new = True
while calc_new:
    print(logo)
    # ask user for a number
    number_one = float(input("What's the first number: "))
    calc_again = True
    while calc_again:
        # print the dict operation
        for operator in operations:
            print(operator)
            # ask user for an operation
        user_operation = input("Pick an operation: " )
            # ask user for a second number
        number_two = float(input("What's the next number?: "))
            #calculate the result
        result = operations[user_operation] (n1=number_one, n2=number_two)
            # print whole calculation
        print(f"{number_one} {user_operation} {number_two} = {result}")
            # ask user to work on with the result
        work_on = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
            # if yes result is going to be the first number
        if work_on == "y":
            number_one = result
            # if no begin a new calculation
        else:
            calc_again = False
            print("\n" * 20)
            calc_new = True




