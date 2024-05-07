'''
Tree needs to satisfy 3 conditions:

1. Each tree has one root node
2. Each node can have multiple children
3. Each node (except root) has one parent
'''

# need to read about trie

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data