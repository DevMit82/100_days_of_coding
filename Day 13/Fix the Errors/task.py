
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You typed in an invalid number. Please type a valid number.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
