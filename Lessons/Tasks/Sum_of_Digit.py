def sum_of_digits(number):
    # Initialize the sum variable
    total = 0

    # Loop through each digit in the number (converted to a string)
    for digit in str(number):
        total += int(digit)  # Convert digit back to int and add to the total

    return total


# Example usage:
number = int(input("Enter a positive integer: "))
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is: {result}")