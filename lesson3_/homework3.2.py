number1 = int(input("Enter firs number ", ))
number2 = int(input("Enter second number ", ))
operation = input("Enter operation with numbers ", )

if operation == '*':
    print (number1 * number2)
elif operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "/":
    if number2 == 0:
        print('Division by zero is impossible')
    else:
        print(number1 / number2)