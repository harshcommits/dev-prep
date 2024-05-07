'''
Two pointer pattern involves using two pointer values in an array
Here we are using that technique to implement an optimized version of two sum problem
It is assumed that the array is already sorted
'''

def two_sum(values, sum):
    pA = values[0]
    pB = values[len(values) - 1]

    # sorting the list
    sorted_values = sorted(values)

    for i in range()