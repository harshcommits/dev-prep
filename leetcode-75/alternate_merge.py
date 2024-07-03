def alternate_merge(word1, word2):
    i = j = 0
    result = ""

    max_index = max(len(word1), len(word2))
    for i in range(0, max_index):
        if i < len(word1) and i < len(word2):
            result += word1[i] + word2[i]

        if i <= len(word1) and i >= len(word2):
            result += word1[i]

        if i >= len(word1) and i <= len(word2):
            result += word2[i]

    return result

if __name__ == "__main__":
    values = alternate_merge("abc", "de")
    print(values)
