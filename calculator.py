
def get_number(message):
    """Read and validate a number from the user."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def calculator():
    """Perform basic arithmetic operations."""
    print("\n--- Basic Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Choose an operation (1-4): ").strip()

    if choice not in ("1", "2", "3", "4"):
        print("Invalid operation choice!")
        return

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    if choice == "1":
        result = num1 + num2
        symbol = "+"
    elif choice == "2":
        result = num1 - num2
        symbol = "-"
    elif choice == "3":
        result = num1 * num2
        symbol = "*"
    else:
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        symbol = "/"

    print(f"Result: {num1:g} {symbol} {num2:g} = {result:g}")


def unit_converter():
    """Convert distance and temperature units."""
    while True:
        print("\n--- Unit Converter ---")
        print("1. Kilometres to Miles")
        print("2. Miles to Kilometres")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. Back to Main Menu")

        choice = input("Choose a conversion (1-5): ").strip()

        if choice == "5":
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice! Please select 1-5.")
            continue

        value = get_number("Enter the value to convert: ")

        if choice == "1":
            result = value * 0.621371
            print(f"{value:g} km = {result:.2f} miles")

        elif choice == "2":
            result = value / 0.621371
            print(f"{value:g} miles = {result:.2f} km")

        elif choice == "3":
            result = (value * 9 / 5) + 32
            print(f"{value:g}°C = {result:.2f}°F")

        elif choice == "4":
            result = (value - 32) * 5 / 9
            print(f"{value:g}°F = {result:.2f}°C")


def main():
    """Display the main menu until the user exits."""
    while True:
        print("\n==============================")
        print(" INTERACTIVE CALCULATOR")
        print("     & UNIT CONVERTER")
        print("==============================")
        print("1. Basic Calculator")
        print("2. Unit Converter")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            unit_converter()
        elif choice == "3":
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
