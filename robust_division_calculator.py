def safe_divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "You cannot divide by zero"
    
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
try:
    print(f"The division of {num1} and {num2} is {safe_divide(num1, num2)}")
except ValueError:
    print("Invalid inputn. Please enter a number.")
except Exception as e:
    print(f"An error occured: {e}")
    