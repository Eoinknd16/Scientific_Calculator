def main():


    def add(x, y):
        return x + y


    print("Select a function")
    print("1.  - ADD -")
    print("2.  - FUNCTION -")

    choice = input("Enter a command, (1/2)")

    num1 = float(input("Enter a number"))
    num2 = float(input("Enter another number"))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))















main()