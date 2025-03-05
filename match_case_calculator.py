#Prompt the user to enter the numbers to be calculated
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#Select your preffered symbol
print("Choose a symbol")
print("1.+")
print("2.-")
print("3.*")
print("4./")

symbol = input()

match symbol:
    case "1":
        print("The sum is ",num1 + num2)
    case "2":
        print("The difference is ", num1 - num2)
    case "3":
        print("The product is ", num1 * num2)
    case "4":
        if num2 == 0:
            print("Division by zero is not possible")
        else:
            print("The division is", num1 / num2)    