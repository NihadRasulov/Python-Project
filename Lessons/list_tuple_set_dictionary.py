"""
List
1.duplicate value
2.mutable
3.indexing

Tuple
1.duplicate value
2.immutable
3. indexing

set
1.non-duplicates
2.mutable
3.non-ordering

dictionary
1.non-duplicate
2.mutable
3.ordering

"""

# def changelist(old_list,index = 0):
#     new_list = []
#     for i in range(len(old_list)):
#         new_list.append(len(old_list[i]))
#     return new_list
#
# a = ["Salam","HowAre You","Hello World"]
# print(changelist(a))


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