FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def get_temperature_input():
    while True:
        try:
            temperature_str = input("Enter the temperature: ")
            temperature = float(temperature_str)  # Try converting to float immediately
            unit = input("Is the temperature in Celsius (C) or Fahrenheit (F)? ").upper()

            if unit not in ("C", "F"):
                print("Invalid unit. Please enter C or F.")
                continue  # Go back to the beginning of the loop

            return temperature, unit

        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

def main():
    temperature, unit = get_temperature_input()

    if unit == "F":
        celsius = convert_to_celsius(temperature)
        print(f"{temperature} Fahrenheit is equal to {celsius:.2f} Celsius")  # Format to 2 decimal places
    elif unit == "C":
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature} Celsius is equal to {fahrenheit:.2f} Fahrenheit") # Format to 2 decimal places


if __name__ == "__main__":
    main()
