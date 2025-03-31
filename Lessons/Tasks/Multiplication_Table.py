
def multiplication_table(num):
    for i in range(1, 11):  # Loop from 1 to 10
        print(str(i) + "x" + str(num) + "=" + str(num * i))  # Print formatted output

# Example usage
multiplication_table(5)