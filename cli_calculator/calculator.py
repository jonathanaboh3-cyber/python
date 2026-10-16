def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def percent(a, b):
    return a % b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


def calculate(first_number, operator, second_number):
    if operator == "+":
        return add(first_number, second_number)

    elif operator == "-":
        return subtract(first_number, second_number)

    elif operator == "%":
        return percent(first_number, second_number)

    elif operator == "*":
        return multiply(first_number, second_number)

    elif operator == "/":
        return divide(first_number, second_number)

    else:
        raise ValueError("Invalid operator.")


def main():
    print("===== PYTHON CLI CALCULATOR =====")
    print("Supported operators: +, -, *, /, %")
    print("Type 'quit' to exit.")

    while True:
        first_input = input("\nEnter first number: ").strip()

        if first_input.lower() == "quit":
            print("Calculator closed.")
            break

        try:
            first_number = float(first_input)

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        operator = input("Enter operator (+, -, *, /, %): ").strip()

        if operator.lower() == "quit":
            print("Calculator closed.")
            break

        if operator not in ["+", "-", "*", "/", "%"]:
            print("Invalid operator.")
            continue

        second_input = input("Enter second number: ").strip()

        if second_input.lower() == "quit":
            print("Calculator closed.")
            break

        try:
            second_number = float(second_input)

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        try:
            result = calculate(
                first_number,
                operator,
                second_number
            )

            print("Result:", result)

        except ZeroDivisionError as error:
            print("Error:", error)

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()