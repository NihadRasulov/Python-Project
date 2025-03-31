def is_armstrong_number(num):
    num_str = str(num)  # Convert number to string
    num_digits = len(num_str)  # Get the number of digits
    total = 0

    # Loop through each digit and calculate the sum of powers
    for digit in num_str:
        total += int(digit) ** num_digits

    # Check if the sum is equal to the original number
    if total == num:
        return True
    else:
        return False


# Example usage
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")