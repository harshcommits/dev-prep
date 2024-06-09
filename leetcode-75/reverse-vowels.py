# this solution sucks, but I came up with it so whatever
def reverse_vowels(value):
    vowels = ['a', 'e', 'i', 'o', 'u']

    vowel_map = {}
    temp_reverse_string = list(value)

    new_positions = []
    letters = []


    for i in range(0, len(value)):
        if value[i] in vowels:
            vowel_map[i] = value[i]
            # intermediate_dict = {i: value[i]}
            # vowel_map.append(intermediate_dict)

        positions = list(vowel_map.keys())
        new_positions = positions[::-1]
        letters = list(vowel_map.values())

        for i in range(0, len(new_positions)):
            temp_reverse_string[new_positions[i]] = letters[i]
            
    print(new_positions)
    print(letters)

    print(vowel_map)

    return "".join(temp_reverse_string)


# This is the saner solution from github using two pointers
def reverse_vowels_sanely(word):
    vowels = "AEIOUaeiou"
    i, j = 0, len(word) - 1
    list_word = list(word)

    while i < j:
        while i < j and list_word[i] not in vowels:
            i += 1
        while i < j and list_word[j] not in vowels:
            j -= 1
        if i < j:
            list_word[i], list_word[j] = list_word[j], list_word[i]
            i, j = i + 1, j - 1

    return "".join(list_word)

if __name__ == "__main__":
    final1 = reverse_vowels('hello') # works
    final2 = reverse_vowels('leetcode')  # works
    final3 = reverse_vowels('Aa')    # doesn't work since upper/lower case is treated the same; might need to incorporate ASCII
    print(final3)
    # print(final)

    # other function
    final4 = reverse_vowels_sanely('Aa')
    print(final4)