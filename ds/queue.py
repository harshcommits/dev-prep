class Queue:
    def __init__(self):
        self.values = []

    def enqueue(self, value):
        self.values.append(0, value)

    def dequeue(self, value):
        if self.values:
            self.values.pop(value)