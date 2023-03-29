from data_structures.tree.helpers import vertical_view
from collections import deque


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


def searchinBST(root_node, node_val):
    if not root_node:
        return print(f"sorry but {node_val} Not found!")

    if node_val == root_node.data:
        return print(f'{node_val} found!')
    elif node_val < root_node.data:
        searchinBST(root_node.left, node_val)
    else:
        searchinBST(root_node.right, node_val)


class AVLnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return str(self.data)


def getHeight(root_node):
    if not root_node:
        return 0
    return root_node.height


def getBalance(root_node):
    if not root_node:
        return 0
    return getHeight(root_node.left) - getHeight(root_node.right)
    # return abs(getHeight(root_node.left) - getHeight(root_node.right))


def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.left
    disbalancedNode.left = disbalancedNode.left.right
    newRoot.right = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.left), getHeight(disbalancedNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot


def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.right
    disbalancedNode.right = disbalancedNode.right.left
    newRoot.left = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.left), getHeight(disbalancedNode.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot


def insertNode(root_node, node_val):
    if not root_node:
        return AVLnode(node_val)

    if node_val < root_node.data:
        temp = insertNode(root_node.left, node_val)
        root_node.left = temp
    elif node_val > root_node.data:
        temp = insertNode(root_node.right, node_val)
        root_node.right = temp

    root_node.height = 1 + max(getHeight(root_node.left), getHeight(root_node.right))
    balance = getBalance(root_node)

    if balance > 1 and node_val < root_node.left.data:  # LL
        return rightRotate(root_node)
    if balance > 1 and node_val > root_node.left.data:  # LR
        root_node.left = leftRotate(root_node.left)
        return rightRotate(root_node)
    if balance < -1 and node_val > root_node.right.data:  # RR
        return leftRotate(root_node)
    if balance < -1 and node_val < root_node.right.data:  # RL
        root_node.right = rightRotate(root_node.right)
        return leftRotate(root_node)

    return root_node


myAVLtree = AVLnode(5)
myAVLtree = insertNode(myAVLtree, 10)
myAVLtree = insertNode(myAVLtree, 15)
myAVLtree = insertNode(myAVLtree, 20)
# insertNode(myAVLtree, 12)
# insertNode(myAVLtree, 13)

vertical_view(myAVLtree)
