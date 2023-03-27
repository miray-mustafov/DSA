from data_structures.tree.helpers import vertical_view
from collections import deque


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrderTraversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    preOrderTraversal(root_node.left)
    preOrderTraversal(root_node.right)


def inOrderTraversal(root_node):
    if not root_node:
        return
    inOrderTraversal(root_node.left)
    print(root_node.data)
    inOrderTraversal(root_node.right)


def postOrderTraversal(root_node):
    if not root_node:
        return
    postOrderTraversal(root_node.left)
    postOrderTraversal(root_node.right)
    print(root_node.data)


def levelOrderTraversal(root_node):
    if not root_node:
        return
    else:
        customQueue = deque([root_node])
        while customQueue:
            root = customQueue.popleft()
            print(root.value.data)
            if root.value.left is not None:
                customQueue.append(root.left)
            if root.value.right is not None:
                customQueue.append(root.right)


def insertinBST(root_node, node_val):
    if not root_node.data:
        root_node.data = node_val

    if node_val <= root_node.data:
        if not root_node.left:
            root_node.left = BSTNode(node_val)
        else:
            insertinBST(root_node.left, node_val)
    else:
        if not root_node.right:
            root_node.right = BSTNode(node_val)
        else:
            insertinBST(root_node.right, node_val)


def searchinBST(root_node, node_val):
    if not root_node:
        return print(f"sorry but {node_val} Not found!")

    if node_val == root_node.data:
        return print(f'{node_val} found!')
    elif node_val < root_node.data:
        searchinBST(root_node.left, node_val)
    else:
        searchinBST(root_node.right, node_val)


my_BST = BSTNode(70)

insertinBST(my_BST, 50)
insertinBST(my_BST, 90)
insertinBST(my_BST, 30)
insertinBST(my_BST, 60)
insertinBST(my_BST, 80)
insertinBST(my_BST, 100)
insertinBST(my_BST, 20)
insertinBST(my_BST, 40)

searchinBST(my_BST, 110)
searchinBST(my_BST, 21)
searchinBST(my_BST, 40)

# vertical_view(my_BST)
