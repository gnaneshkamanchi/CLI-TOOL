# CLI-TOOL

# Why is the Calculator a CLI Tool?

## 1. Command-Line Based
- The calculator operates entirely in a terminal or command prompt.
- Users interact with the program by entering inputs (choices and numbers) via the keyboard.

## 2. User Input and Output
- Users input commands (like selecting options from the menu) directly into the terminal.
- The tool processes the input and returns the output (e.g., the result of a calculation) in text format.

## 3. Lightweight
- There’s no GUI (Graphical User Interface) for buttons or windows; it relies on simple text-based interaction.

## 4. Automatable
- Although simple, the calculator could be extended to work with scripts or accept command-line arguments for automation.


# Python Calculator

## How the Program Works

### 1. User Interface
- A menu is displayed to the user with 6 options:
  - Addition
  - Subtraction
  - Multiplication
  - Division
  - Modulus
  - Exit

### 2. User Input
- The user selects an operation (1–6).
- If the user inputs invalid data (e.g., letters), it shows an error and prompts again.

### 3. Numeric Inputs
- The program takes two numeric inputs for the operation.
- It uses `float()` to handle both integers and decimal numbers.

### 4. Perform Operations
- Based on the user's choice:
  - **Addition**: Adds `num1 + num2`
  - **Subtraction**: Subtracts `num1 - num2`
  - **Multiplication**: Multiplies `num1 * num2`
  - **Division**: Checks for division by zero to prevent errors; otherwise, calculates `num1 / num2`
  - **Modulus**: Computes the remainder of `num1 % num2`.

### 5. Error Handling
- Includes exception handling (`try-except`) for invalid inputs.
- Prevents division by zero and catches non-numeric input errors.

### 6. Loop and Exit
- The program runs in a loop until the user selects option `6` to exit.
