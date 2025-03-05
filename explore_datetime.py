import datetime

def display_current_datetime():

   current_datetime = datetime.datetime.now()

   formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

   print(f"Current date and time: {formatted_datetime}")

if __name__ == "__main__":  # This ensures the function is only called when the script is run directly.
    display_current_datetime()

Number_of_days = int(input("Enter the day: "))

def  calculate_future_date(current_date):
    """Calculates and displays the future date after a user-specified number of days."""
    while True:  # Input validation loop
        try:
            days_to_add = int(input("Enter the number of days to add: "))
            if days_to_add >=0: #check if the number of day is not negative
                break
            else:
                print("Please enter a non-negative integer number of days.")

        except ValueError:
            print("Invalid input. Please enter an integer.")

    future_date = current_date + datetime.timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future Date:", formatted_future_date)

