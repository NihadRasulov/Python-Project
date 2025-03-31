def count_word_frequency(input_string):
    word_count = {}
    words = input_string.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


# Example usage
input_string = "This is a test This a test"
result = count_word_frequency(input_string)
print(result)