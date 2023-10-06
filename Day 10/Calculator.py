import arts

# Add
def add(n1, n2):
    return n1 + n2


# Substract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def dvide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": dvide
}

def calculator():
    print(arts.logo)
    num1 = float(input("What's the first number?: "))
    
    for key in operations:
        print(key)

    stop_calculation = True

    while stop_calculation:
        
        operation_symbol = input("Pick an operation: ")   
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)


        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' continue calculating with {answer}, or 'n to exit.: ") == "y":
            num1 = answer
        else:
            stop_calculation = False
            calculator()

calculator()        