# def is_prime(number):
#     if number <= 1 or number > 100:
#         return False  # Prime numbers are greater than 1 and less than or equal to 100
#     for i in range(2, int(number ** 0.5) + 1):  # Check divisibility up to the square root of the number
#         if number % i == 0:
#             return False  # If divisible by any number, it's not prime
#     return True  # If no divisors found, the number is prime
#
# num = int(input("Enter a number (1 to 100): "))
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")


def is_prime(number):
    if number <= 1 or number > 100:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(is_prime(10))

# Example usage
# num = int(input("Enter a number (1 to 100): "))
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")