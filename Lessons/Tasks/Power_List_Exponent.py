def power_list(numbers, exponent):
    result = []  # Initialize an empty list to store results
    for num in numbers:
        result.append(num ** exponent)  # Raise each number to the power of exponent
    return result

# Example usage:
numbers = [2, 3, 4, 5]
exponent = int(input("enter the exponent"))
print(power_list(numbers, exponent))

