# def pyramid_numbers():
#     for i in range(1, 11):
#         for j in range(1, i + 1):
#             print(j, end = " ")
#         print()
# pyramid_numbers()

# def print_number_pyramid():
#     current_number = 1
#     total_numbers = 10
#     rows = 4
#     max_width = 4 * 2 + 3
#
#     for row in range(1, rows + 1):
#         asterisks = (rows - row) * 2
#
#         for _ in range(asterisks):
#             print(" ", end="")
#
#         numbers_in_row = row
#         for i in range(numbers_in_row):
#             if current_number > total_numbers:
#                 break
#             print(f"{current_number:2}", end="")
#             current_number += 1
#             if i < numbers_in_row - 1:
#                 print(" ", end="")
#
#         print()
#
# print_number_pyramid()


def print_number_pyramid(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        numbers = ' '.join(str(num) for num in range(1, i + 1))
        print(spaces + numbers)

print_number_pyramid(10)