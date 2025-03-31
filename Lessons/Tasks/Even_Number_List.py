def filter_even_numbers(lst):
    even_numbers = []
    for num in lst:
        if num % 2 == 0:  # Check if the number is even
            even_numbers.append(num)  # Add to result list
    return even_numbers

# Example usage
numbers = [1, 2, 3, 4, 5, 6]
print(filter_even_numbers(numbers))