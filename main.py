# Define a function for the calculator
def calculator():
    print("Welcome to the Python Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exit")

    while True:
        try:
            # Prompt user for operation choice
            choice = input("\nEnter your choice (1-6): ")
            
            # Check for exit condition
            if choice == '6':
                print("Exiting the calculator. Goodbye!")
                break

            # Validate the choice
            if choice not in ['1', '2', '3', '4', '5']:
                print("Invalid choice. Please enter a number between 1 and 6.")
                continue

            # Prompt user for two numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the chosen operation
            if choice == '1':
                print(f"The result of addition: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"The result of subtraction: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"The result of multiplication: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                # Handle division by zero
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"The result of division: {num1} / {num2} = {num1 / num2}")
            elif choice == '5':
                print(f"The result of modulus: {num1} % {num2} = {num1 % num2}")
        
        except ValueError:
            # Handle invalid input for numbers
            print("Error: Please enter valid numeric values.")

# Run the calculator program
calculator()
