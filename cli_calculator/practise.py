# def store_details(name, number1, number2):
#     print("Name:", name)
#     print("First number:", number1)
#     print("Second number:", number2)

# store_details("jonathan", 10, 12)


# def my(x, y):
#     return float (x + y)

# result = my("5", "3")    
# print(result)

# def calculate():
#     num1 = (input("enter first number"))
#     operator = input("+, -, *, /")
#     num2 = (input("enter second number"))

#     if operator == "+":
#        return (num1 + num2)

#     elif operator == "-":
#          return (num1 - num2)

def calculate():
    num1 = int(input("Enter first number: "))
    operator = input("Choose an operation (+, -, *, /): ")
    num2 = int(input("Enter second number: "))

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return "Can't be divided by zero"
        return num1 / num2

    else:
        return "Invalid operator"


result = calculate()
print(result)