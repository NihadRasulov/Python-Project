char = input("Enter a single character: ")

if len(char) != 1:
    print("Error: Please enter only one character.")
else:
    print(f"The ASCII value of '{char}' is {ord(char)}")

