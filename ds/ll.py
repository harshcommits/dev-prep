class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.data

    def set_next(self, node):
        self.next = node

    def next_value(self):
        return self.next

class LL:
    def __init__(self):
        self.head = None

    def add_value(self, value):

        node = LLNode(value)

        if self.head == None:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.get_next()
            
        current.next = node