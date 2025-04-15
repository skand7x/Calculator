from art import logo

def add(n1, n2):
    """Performs addition on both the numbers"""
    return n1 + n2

def subtract(n1, n2):
    """Performs subtraction on both the numbers"""
    return n1 - n2

def multiply(n1, n2):
    """Performs multiplication on both the numbers"""
    return n1 * n2

def divide(n1, n2):
    """Performs division on both the numbers"""
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide} #The dictionary storing the functions as values and their symbols as keys

while True :
    print(logo)
    first_number = float(input("Please enter your first number: "))

    operator = input("+\n-\n*\n/\nPlease choose an operation: ")

    second_number = float(input("Please enter your second number: "))

    result = operations[operator](first_number,second_number)


    should_continue = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")

    if should_continue == "y":
        continue_calc = True
        while continue_calc is True:
            first_number = result
            operator = input("+\n-\n*\n/\nPlease choose an operation: ")
            second_number = float(input("Please enter your next number: "))
            result = operations[operator](first_number, second_number)
            print(f"{first_number} {operator} {second_number} = {result}")
            should_continue = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")
            if should_continue == "n":
                break
    if should_continue == "n":
        continue
















