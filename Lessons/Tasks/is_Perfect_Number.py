def is_perfect_number(num):
    if num <= 1:
        return False

    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:  # Check if i is a divisor of num
            divisors_sum += i  # Add divisor to sum

    # Check if the sum of divisors equals the original number
    return divisors_sum == num


# Example usage
number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(f"{number} is a Perfect number.")
else:
    print(f"{number} is not a Perfect number.")