def perform_operation(num1, num2, operation):

    if operation == "add":
        return num1 + num2
    
    elif operation == "subtract":
        return num1 - num2
    
    elif operation == "multiply":
        return num1 * num2
    
    elif operation == "divide":
        return num1 / num2
    if operation == "modulus":
        return num1 % num2
    else:
        return "Invalid operation"