def count_vowels(word):
    word = word.lower()
    vowels = "aeiou"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

# Example usage
word = input("Enter a word: ")
print("Number of vowels:", count_vowels(word))
