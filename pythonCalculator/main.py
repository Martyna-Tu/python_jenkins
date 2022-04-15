# Program make a simple calculator
import sys

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y

if __name__ == "__main__":

    while True:
        # take input from the user
        choice = sys.argv[1]
        # check if choice is one of the four options
        if choice in ('Add', 'Sub', 'Div', 'Mul'):
            num1 = float(sys.argv[2])
            num2 = float(sys.argv[3])

            if choice == 'Add':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == 'Sub':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == 'Mul':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == 'Div':
                print(num1, "/", num2, "=", divide(num1, num2))

            break

