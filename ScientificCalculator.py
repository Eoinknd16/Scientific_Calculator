# CODE IS GLITCHY FIX IF YOU CAN

# EXPONENTIAL FUNCTION IS BROKEN
def main():
    import math

# defining all the functions.

    def add(x, y):
            return x + y

    def subtract(x, y):
            return x - y

    def square(x):
            return x * x

    def multiply(x, y):
            return x * y

    def exp(x):
            return math.exp(x)

    def power(x, y):
        return x ** y

    def divide(x, y):
        return x / y

    def pi(x, y):
        return x * y

    def sqrt(x):
        return math.sqrt(x)

    def sin(x):
        return math.sin(x)

    def cos(x):
        return math.cos(x)

    def tan(x):
        return math.tan(x)

    def log(x):
        return math.log(x, 10)

    # Basic input demands for user.

    print("Select a function")
    print("1.  - ADD -")
    print("2.  - subtract -".upper())
    print("3.  - SQUARE -")
    print("4.  - MULTIPLY -")
    print("5.  - EXPONENTIATE")
    print("6.  - POWER - ")
    print("7.  - DIVIDE - ")
    print("8.  - PI - ")
    print("9.  - SQUARE ROOT - ")
    print("10.  - SIN - ")
    print("11.  - COS - ")
    print("12.  - TAN - ")
    print("13.  - LOG_BASE 10 - ")

    # Input for choosing a mode

    choice = input("Enter a command, (1/2/3/4/5/6/7)")

    # This is where the user enters the numbers they are using on the calculator

    if choice == '1':
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        print("ANSWER: ", num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        print("ANSWER: ", num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        num1 = float(input("Enter a number: "))
        print("ANSWER: ", num1, "^2", "=", square(num1))

    elif choice == '4':
        num1 = float(input("Enter at number: "))
        num2 = float(input("Enter another number: "))
        print("ANSWER: ", num1, "", num2, "=", multiply(num1, num2))
    elif choice == '5':
        num1 = float(input("Enter a number: "))
        print("ANSWER: ", num1, "**", "=", exp(num1))

    elif choice == '6':
        num1 = float(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        print("ANSWER: ", num1, "^", num2, "=", power(num1, num2))

    elif choice == '7':
        num1 = float(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        print("ANSWER: ", num1, "/", num2, "=", divide(num1, num2))

    elif choice == '8':
        num1 = float(input("Enter a number: "))
        num2 = float(3.14)
        print("ANSWER: ", num1, "*", num2, "=", pi(num1, num2))

    elif choice == '9':
        num1 = float(input("Enter a number: "))
        print("ANSWER: ", num1, "root", "=", sqrt(num1))

    elif choice == '10':
        num1 = float(input("Enter a number: "))
        print("ANSWER: ", num1, "sin(x)", "=", sin(num1))

    elif choice == '11':
        num1 = float(input("Enter a number: "))
        print("ANSWER: ", num1, "cos(x)", "=", cos(num1))

    elif choice == '5318008':
        print("BOOBIES")

    elif choice == '12':
        num1 = float(input("Enter a number: "))
        print("ANSWER: ", num1, "tan(x)", "=", tan(num1))

    elif choice == '13':
        num1 = float(input("Enter a number: "))
        print("ANSWER: ", num1, "log(x)", "=", log(num1))

while True:

      restart = input("Do you wish to start calculating? [y/n]")
      if restart == "y":
        main()

      else:
        exit()
