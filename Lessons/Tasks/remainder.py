def find_remainder():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        remainder = num1 % num2
        print(f"The remainder when {num1} is divided by {num2} is: {remainder}")

find_remainder()