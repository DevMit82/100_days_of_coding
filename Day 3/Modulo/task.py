#ask for number and convert it to int and store it in  a variable called number
number = int(input("Please write a number\n"))

#if there is no remainder, the number have to be even else it is odd
if number % 2 == 0 :
    print("Number is even.")
else:
    print("Number is odd")