# leetcode solution inspired
def move_zeroes(num):
    left = 0
    for right in range(len(num)):
        print(left)
        if num[right] != 0:
            print("Swap:", left, right)
            num[right], num[left] = num[left], num[right]
            left += 1

    return num


if __name__ == "__main__":
    sample = [0, 1]
    sample2 = [0, 1, 0, 3, 12]
    # print(move_zeroes(sample))
    print(move_zeroes(sample2))