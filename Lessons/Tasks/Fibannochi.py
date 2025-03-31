def fibonacci_until_n(limit):
    a, b = 0, 1
    while a <= limit:
        print(a, end=" ")
        a, b = b, a + b

num = int(input("Enter a number: "))
fibonacci_until_n(num)