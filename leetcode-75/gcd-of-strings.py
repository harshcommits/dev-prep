def gcdOfStrings(str1, str2):
    len1, len2 = len(str1), len(str2)

    def valid(k):
        if len1 % k or len2 % k:
            return False
        
        n1, n2 = len1 // k, len2 // k
        base = str1[:k]

        # print(str1 == n1 * base and str2 == n2 * base)
        return str1 == n1 * base and str2 == n2 * base

    for i in range(min(len1, len2), 0, -1):
        if valid(i):
            return str1[:i] 


if __name__ == "__main__":
    print(gcdOfStrings("ABABAB", "AB"))
    print(gcdOfStrings("ABABAB", "CODE"))