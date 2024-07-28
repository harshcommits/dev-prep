def reverseWords(s: str) -> str:
        words = []
        i, n = 0, len(s)
        print(n)
        while i < n:
            print(words)
            while i < n and s[i] == " ":
                print("i:", i)
                print(s[i])
                i += 1
            if i < n:
                j = i
                print("j: ", j)
                print(s[j])
                while j < n and s[j] != " ":
                    j += 1
                print("string: ", s[i:j])
                words.append(s[i:j])
                i = j
        return " ".join(words[::-1])

if __name__ == "__main__":
    s = " Whatever it takes "
    print(reverseWords(s))