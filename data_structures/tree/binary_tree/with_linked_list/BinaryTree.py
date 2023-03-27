from collections import deque
from data_structures.tree.binary_tree.with_linked_list.bitree_traversals import levelorder_traversal_defaultdict
from data_structures.tree.helpers import vertical_view

"""
this is my code for binary tree. Can you give me a 
function that vizualizes VERTICALLY my_binary_tree 
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return "n" + self.data


def searchinBT(tree_node, node_data):  # its level order traversal
    if not tree_node: return

    customQueue = deque([tree_node])
    while customQueue:
        cur_node = customQueue.popleft()
        if node_data == cur_node.data:
            return cur_node
        if cur_node.left:
            customQueue.append(cur_node.left)

        if cur_node.right:
            customQueue.append(cur_node.right)
    return 'Not found'


def insert1by1BT(tree_node, new_node):
    if not tree_node: return

    customQueue = deque([tree_node])
    while customQueue:
        cur_node = customQueue.popleft()
        if cur_node.left:
            customQueue.append(cur_node.left)
        else:
            cur_node.left = new_node
            return print(f"{new_node} left child added")

        if cur_node.right:
            customQueue.append(cur_node.right)
        else:
            cur_node.right = new_node
            return print(f"{new_node} right child added")


def getdeepestNode(root_node):
    if not root_node: return
    root = None
    customQueue = deque([root_node])
    while customQueue:
        root = customQueue.popleft()
        if root.left:
            customQueue.append(root.left)
        if root.right:
            customQueue.append(root.right)
    return root


def delete_deepestNode(root_node, deepest_node):
    if not root_node: return
    if root_node is deepest_node:
        root_node.data = None
        return

    customQueue = deque([root_node])
    while customQueue:
        root = customQueue.popleft()

        if root.right:
            if root.right == deepest_node:
                root.right = None
                return
            else:
                customQueue.append(root.right)
        if root.left:
            if root.left == deepest_node:
                root.left = None
                return
            else:
                customQueue.append(root.left)


def deleteNode(root_node, node_value):
    if not root_node: return

    if root_node.data == node_value:  # trying to delete the main root
        deleteBT(root_node)

    customQueue = deque([root_node])
    while customQueue:
        root = customQueue.popleft()
        if root.data == node_value:
            dNode = getdeepestNode(root)
            root.data = dNode.data
            delete_deepestNode(root, dNode)
            return print(f"{node_value} was deleted!")
        if root.left:
            customQueue.append(root.left)
        if root.right:
            customQueue.append(root.right)

    return print('Wrong node_value specified!')


def deleteBT(root_main):
    root_main.left = None
    root_main.right = None
    root_main.data = None
    return print("Root main deleted!")


my_binary_tree = Node("Pets")

my_binary_tree.left = Node('Cat')
my_binary_tree.right = Node('Dog')

my_binary_tree.left.left = Node('Egyptian')
persian = Node('Persian')
my_binary_tree.left.right = persian

persian.left = Node('Blue')
persian.right = Node('Black')

my_binary_tree.right.left = Node('Chau Chau')
my_binary_tree.right.right = Node('Pekines')

print()

levelorder_traversal_defaultdict(my_binary_tree)
# deleteBT(my_binary_tree)
vertical_view(my_binary_tree)
