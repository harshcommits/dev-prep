# def reverse_strings(value):
#     reverse = []
#     cleaner = value.strip()
#     array_words = cleaner.split(" ")
#     print(array_words)
#     for word in cleaner:
#         reverse.append(word)

#     return "".join(reverse)

# if __name__ == "__main__":
#     example

# example = "The sky is blue"
example = "a good   example"

cleaner = ' '.join(example.split())

# cleaner = example.strip()
array_of_words = cleaner.split()

print(" ".join(array_of_words[::-1]))