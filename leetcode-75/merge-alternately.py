def mergeAlternately(word1, word2):
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

# another way to do it
def mergeAlternatelyPartTwo(word1, word2):
    merged = ""
    w1 = len(word1)
    w2 = len(word2)
    l = min(w1, w2)
    for i in range(l):
        merged += word1[i] + word2[i]
    if w1 == w2:
        return merged
    elif w1 > w2:
        return merged + word1[l:]
    elif w1 < w2:
        return merged + word2[l:]


if __name__ == "__main__":
    # values = mergeAlternately("abc", "de")
    values = mergeAlternatelyPartTwo("abc", "de")
    print(values)