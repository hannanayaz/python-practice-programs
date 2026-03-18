def calculator():
    num1 = float(input("First number: "))
    op = input("Operator (+, -, *, /): ")
    num2 = float(input("Second number: "))

    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        print("Result:", num1 / num2)
    else:
        print("Invalid operator")

calculator()
