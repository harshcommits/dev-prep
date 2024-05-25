def solution(A):
    # Implement your solution here
    # pass
    max_value = max(A)

    if max_value < 0:
        return 1
    else:
        missing_values = []
        for value in range(1, max_value):
            if value not in A:
                missing_values.append(value)

        return min(missing_values)
        
if __name__ == "__main__":
    A = [1, 3, 6, 4, 1, 2]
    print(solution(A))