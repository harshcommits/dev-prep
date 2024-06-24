import time

# brute force method; efficiency is O(n2)
def two_sum(values, sum):
    for i in range (0, len(values)-1):
        for j in range(i+1, len(values)):
            if values[i] +  values[j] == sum:
                return f"The values are {values[i]} and {values[j]}"

    return "no such values exist"

# the more optimized approach
def two_sum_better(values, sum):
    i, j = 0, len(values) - 1
    while (i != j): # doesn't work with odd no. of values, misses the middle element because of logic flaw
        if values[i] + values[j] == sum:
            return f"The better values are {values[i]} and {values[j]}"
        
        i += 1
        j -= 1

    return "no such values exist"


if __name__ == "__main__":
    
    values = [1, 2, 4, 5, 67, 3]

    print(two_sum(values, 4))
    print(two_sum_better(values, 4))