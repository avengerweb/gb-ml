import operator

print("Calculator")
print("Available operators: -, +, *, / or 0 for exit")
print("We hope you are good user!")

while True:
    action = input("Enter operator (0 for exit): ")

    if action == "0":
        print("Bye")
        break
    elif action == "+":
        action = operator.add
    elif action == "-":
        action = operator.sub
    elif action == "/":
        action = operator.truediv
    elif action == "*":
        action = operator.mul
    else:
        action = None

    if action is None:
        continue

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num2 == 0 and action == operator.truediv:
        print("We can`t divide by zero!")
        continue

    print(f"Result: {action(num1, num2)}")
