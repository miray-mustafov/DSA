from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return "n"+self.data

def searchinBT(tree_node, node_data):
    if not tree_node:
        return
    else:
        customQueue = deque([tree_node])

        while customQueue:
            root = customQueue.popleft()
            if node_data == root.data:
                return root
            if (root.left_child is not None):
                customQueue.append(root.left_child)

            if (root.right_child is not None):
                customQueue.append(root.right_child)

my_binary_tree = Node("Pet")

my_binary_tree.left_child = Node('Cat')
my_binary_tree.right_child = Node('Dog')

my_binary_tree.left_child.left_child = Node('Egyptian cat')
my_binary_tree.left_child.right_child = Node('Persian cat')

my_binary_tree.right_child.left_child = Node('Chau Chau')
my_binary_tree.right_child.right_child = Node('Pekines')

print(searchinBT(my_binary_tree, "Pekines"))