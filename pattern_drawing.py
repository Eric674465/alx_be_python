# Prompt the user to enter a positive integer for the pattern size
size = int(input("Enter the size of the pattern: "))

# Validate the input
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize a counter for the rows
    row = 0

    # Outer loop: Iterate through each row
    while row < size:
        # Inner loop: Print '*' for each column in the current row
        for _ in range(size):
            print("*", end="")  # Print '*' without moving to a new line
        print()  # Move to the next line after completing the row
        row += 1  # Increment the row counter