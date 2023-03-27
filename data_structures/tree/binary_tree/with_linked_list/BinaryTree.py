from graphviz import Digraph

from collections import deque
from data_structures.tree.binary_tree.with_linked_list.bitree_traversals import levelorder_traversal_defaultdict

"""
this is my code for binary tree. Can you give me a 
function that vizualizes VERTICALLY my_binary_tree 
"""


def vertical_view(root_node):
    if not root_node.left_child or not root_node.right_child:
        return print("tree empty")
    dot = Digraph()

    # helper function to draw each node and its children
    def draw_node(node):
        if not node:
            return
        dot.node(node.data)
        if node.left_child:
            dot.edge(node.data, node.left_child.data)
            draw_node(node.left_child)
        if node.right_child:
            dot.edge(node.data, node.right_child.data)
            draw_node(node.right_child)

    draw_node(root_node)
    dot.render(view=True)


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return "n" + self.data


def searchinBT(tree_node, node_data):  # its level order traversal
    if not tree_node: return

    customQueue = deque([tree_node])
    while customQueue:
        cur_node = customQueue.popleft()
        if node_data == cur_node.data:
            return cur_node
        if cur_node.left_child:
            customQueue.append(cur_node.left_child)

        if cur_node.right_child:
            customQueue.append(cur_node.right_child)
    return 'Not found'


def insert1by1BT(tree_node, new_node):
    if not tree_node: return

    customQueue = deque([tree_node])
    while customQueue:
        cur_node = customQueue.popleft()
        if cur_node.left_child:
            customQueue.append(cur_node.left_child)
        else:
            cur_node.left_child = new_node
            return print(f"{new_node} left child added")

        if cur_node.right_child:
            customQueue.append(cur_node.right_child)
        else:
            cur_node.right_child = new_node
            return print(f"{new_node} right child added")


def getdeepestNode(root_node):
    if not root_node: return
    root = None
    customQueue = deque([root_node])
    while customQueue:
        root = customQueue.popleft()
        if root.left_child:
            customQueue.append(root.left_child)
        if root.right_child:
            customQueue.append(root.right_child)
    return root


def delete_deepestNode(root_node, deepest_node):
    if not root_node: return
    if root_node is deepest_node:
        root_node.data = None
        return

    customQueue = deque([root_node])
    while customQueue:
        root = customQueue.popleft()

        if root.right_child:
            if root.right_child == deepest_node:
                root.right_child = None
                return
            else:
                customQueue.append(root.right_child)
        if root.left_child:
            if root.left_child == deepest_node:
                root.left_child = None
                return
            else:
                customQueue.append(root.left_child)


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
        if root.left_child:
            customQueue.append(root.left_child)
        if root.right_child:
            customQueue.append(root.right_child)

    return print('Wrong node_value specified!')


def deleteBT(root_main):
    root_main.left_child = None
    root_main.right_child = None
    root_main.data = None
    return print("Root main deleted!")


my_binary_tree = Node("Pets")

my_binary_tree.left_child = Node('Cat')
my_binary_tree.right_child = Node('Dog')

my_binary_tree.left_child.left_child = Node('Egyptian')
persian = Node('Persian')
my_binary_tree.left_child.right_child = persian

persian.left_child = Node('Blue')
persian.right_child = Node('Black')

my_binary_tree.right_child.left_child = Node('Chau Chau')
my_binary_tree.right_child.right_child = Node('Pekines')

insert1by1BT(my_binary_tree, Node("New Left")),
insert1by1BT(my_binary_tree, Node("New Right")),
print()
# deleteNode(my_binary_tree, 'Cat')

levelorder_traversal_defaultdict(my_binary_tree)
deleteBT(my_binary_tree)
vertical_view(my_binary_tree)
