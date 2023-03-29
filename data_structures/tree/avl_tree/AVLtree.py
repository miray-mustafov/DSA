from data_structures.tree.helpers import vertical_view
from collections import deque


def levelOrderTraversal(root_node):
    if not root_node:
        return
    else:
        customQueue = deque([root_node])
        while customQueue:
            root = customQueue.popleft()
            print(root.data, root.height)
            if root.left is not None:
                customQueue.append(root.left)
            if root.right is not None:
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


def getHeight(root_node):
    if not root_node:
        return 0
    return root_node.height


def getBalance(root_node):
    if not root_node:
        return 0
    return getHeight(root_node.left) - getHeight(root_node.right)
    # return abs(getHeight(root_node.left) - getHeight(root_node.right))


def getMinValue(root_node):
    if not root_node or not root_node.left:
        return root_node
    return getMinValue(root_node.left)


def deleteNode(root_node, node_val):
    if not root_node:
        return root_node

    if node_val < root_node.data:
        root_node.left = deleteNode(root_node.left, node_val)
    elif node_val > root_node.data:
        root_node.right = deleteNode(root_node.right, node_val)
    else:
        if root_node.left is None:
            temp = root_node.right
            root_node = None
            return temp

        if root_node.right is None:
            temp = root_node.left
            root_node = None
            return temp

        temp = getMinValue(root_node.right)
        root_node.data = temp.data
        root_node.right = deleteNode(root_node.right, temp.data)

    # !!!!!!!!!!!!!
    root_node.height = 1 + max(getHeight(root_node.left), getHeight(root_node.right))
    balance = getBalance(root_node)

    if balance > 1 and getBalance(root_node.left) >= 0:
        return rightRotate(root_node)
    if balance < -1 and getBalance(root_node.right) <= 0:
        return leftRotate(root_node)
    if balance > 1 and getBalance(root_node.left) < 0:
        root_node.left = leftRotate(root_node.left)
        return rightRotate(root_node)
    if balance < -1 and getBalance(root_node.right) > 0:
        root_node.right = rightRotate(root_node.right)
        return leftRotate(root_node)

    return root_node

def deleteAVL(root_node):
    root_node.left = None
    root_node.right = None
    root_node.data = None

myAVLtree = AVLnode(50)
myAVLtree = insertNode(myAVLtree, 70)
myAVLtree = insertNode(myAVLtree, 80)
myAVLtree = insertNode(myAVLtree, 40)
myAVLtree = insertNode(myAVLtree, 60)
myAVLtree = insertNode(myAVLtree, 30)
myAVLtree = insertNode(myAVLtree, 20)
myAVLtree = insertNode(myAVLtree, 10)
myAVLtree = insertNode(myAVLtree, 35)
myAVLtree = insertNode(myAVLtree, 45)
myAVLtree = insertNode(myAVLtree, 25)
myAVLtree = insertNode(myAVLtree, 65)
myAVLtree = insertNode(myAVLtree, 55)

myAVLtree = deleteNode(myAVLtree, 80)
myAVLtree = deleteNode(myAVLtree, 55)
myAVLtree = deleteNode(myAVLtree, 60)
myAVLtree = deleteNode(myAVLtree, 65)
# myAVLtree = deleteNode(myAVLtree, 70)


vertical_view(myAVLtree)
