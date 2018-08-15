#### CODE IS GLITCHY FIX IF YOU CAN ####


def main():

#### defining all the functions.

    def add(x, y):
            return x + y

    def subtract(x, y):
            return x - y

    def square(x):
            return x * x

    def multiply(x, y):
            return x * y

    #### Basic input demands for user.

    print("Select a function")
    print("1.  - ADD -")
    print("2.  - subtract -".upper())
    print("3.  - SQUARE -")
    print("4.  - MULTIPLY -")

    #### Input for choosing a mode

    choice = input("Enter a command, (1/2/3)")

    #### This is where the user enters the numbers they are using on the calculator

    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number:  \n\n(if anothr number is not required then just enter any number it will be ignored by the code)"))

    if choice == '1':
             print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
            print(num1, "^2", "=", square(num1))

    elif choice == '4':
            print(num1, "*", num2, "=", multiply(num1, num2))

restart = input("Do you wish to restart? [y/n]")
if restart == "y":
     main()

else:
    exit()



main()
