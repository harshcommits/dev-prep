from ds import stack, queue, ll

if __name__ == "__main__":
    stck = stack.Stack()
    values = [1, 3, 5, 6]

    for value in values:
        stck.push(value)

    print(stck.pop())
    for value in stck.values:
        print(value)