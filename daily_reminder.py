task_variable = input("Enter your task: ")
priority_variable = input("Priority(high/medium/low) ")
time_bound = input("Is it time bound? (yes/no) ")
match priority_variable:
    case "high" if  time_bound == "yes":
        print(f"{task_variable} is a high priority so it requires immediate attention today.")
    case "high" if time_bound == "no":
        print*(f"{task_variable} is a priority but it can be compromised")    
    case "medium" if time_bound == "no":
        print(f"{task_variable} is a medium priority so it  rquires less attention.")
    case "medium" if time_bound == "yes":
        print(f"{task_variable} is a relative priority but it can not be delayed")    
    case "low" if time_bound == "no":
        print(f"{task_variable} is a low priority so do it at your leisure time")   
    case "low" if time_bound == "yes":
        print(f"{task_variable} is a low priority so it can be done when you are free") 
    case "_":
        print("Invalid entry")    