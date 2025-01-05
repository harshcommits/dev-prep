def greatest_no_of_candies(candies, extraCandies):
    result = []

    for i in candies:
        if extraCandies + i >= max(candies):
            result.append(True)
        else:
            result.append(False)

    return result


if __name__ == "__main__":
    candies = [2,3,5,1,3]
    extraCandies = 3
    print(greatest_no_of_candies(candies, extraCandies))