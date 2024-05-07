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

    def search(self, target):
        if self.data == target:
            print('Found it')
            return self
        
        if self.left and self.data > target:
            return self.left.search(target)
        
        if self.right and self.data < target:
            return self.right.search(target)
        
        print('Value is not in tree')

class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):  # allows avoiding mentioning the root keyword for searching data, as was done on line 58
        return self.root.search(target)


node = Node(20)
node.right = Node(25)
node.left = Node(15)

node.left.left = Node(10)
node.left.right = Node(17)

node.right.left = Node(22)
node.right.right = Node(30)

print(node.right.right.data)
print(node.right.data)


myTree = Tree(node, 'My Tree')
print(myTree.root.right.data)
print(myTree.root.right.right.data)
print(myTree.name)

# found = myTree.root.search(30)
found = myTree.search(31)
# print(found.data)