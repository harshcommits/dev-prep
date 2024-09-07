class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        return self.values.append(value)

    def pop(self):
        return self.values.pop()

