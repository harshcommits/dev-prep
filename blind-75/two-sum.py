# brute force method; efficiency is O(n2)
def two_sum(values, sum):
    for i in range (0, len(values)-1):
        for j in range(i+1, len(values)-1):
            if values[i] +  values[j] == sum:
                return f"The respective numbers are {values[i]} and {values[j]}"

    return "The values don't exist"


if __name__ == "__main__":
    
    values = [1, 2, 4, 5, 67]
    print(two_sum(values, 10))