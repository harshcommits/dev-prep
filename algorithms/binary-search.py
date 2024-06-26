def binary_search(values, value, low, high):

    if high >= low:

        mid = (low + high) // 2

        if values[mid] == value:
            return mid
        elif values[mid] < value:
            return binary_search(values, value, mid+1, high)
        else:
            return binary_search(values, value, low, mid - 1)
    
    else:
        return -1

if __name__ == "__main__":
    values = [1, 2, 4, 5, 6]
    result = binary_search(values, 25, 0, len(values)-1)
    if result == -1:
        print("Value not in list")
    else:
        print("The value is at {result}")