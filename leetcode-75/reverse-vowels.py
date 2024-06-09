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

if __name__ == "__main__":
    final = reverse_vowels('hello') # works
    final = reverse_vowels('leetcode')  # works
    final = reverse_vowels('Aa')    # doesn't work since upper/lower case is treated the same; might need to incorporate ASCII
    print(final)
    # print(final)