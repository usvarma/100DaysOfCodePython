from art import logo


# Add two numbers
def add(num1, num2):
    return num1 + num2


# Subtract a number from another number
def subtract(num1, num2):
    return num1 - num2


# Multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Divide a number by another number
def divide(num1, num2):
    return num1 / num2


operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

operations_string = {'+': "Add", '-': "Subtract", '*': "Multiply", '/': "Divide"}


def calculator():
    print(logo)
    continue_operations = True
    num1 = float(input("Enter the first number: \n"))
    current_result = num1

    while continue_operations:
        previous_result = current_result
        print("Choose an operation to perform: \n")

        for ops in operations:
            print(f"{ops} to {operations_string[ops]}")

        user_op = input("\n")
        num2 = float(input("Enter the second number: \n"))

        current_result = operations[user_op](current_result, num2)
        print(
            f"Result of operation {operations_string[user_op]} ({user_op}) on two numbers {previous_result} and {num2} is {current_result}")

        continue_calc = input(f"Type 'y' to continue calculations with {current_result} or 'n' to quit: \n")

        if continue_calc != 'y':
            continue_operations = False
            calculator()


if __name__ == '__main__':
    calculator()
