from data_structures.tree.helpers import vertical_view

from collections import deque


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __repr__(self):
        return f"({self.val})" + str(self.next)


class BinaryTree:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def levelOrderTraversal(self):
        if not self:
            return

        customQueue = deque([self])
        while customQueue:
            root = customQueue.popleft()
            print(root.data)
            if root.left:
                customQueue.append(root.left)
            if root.right:
                customQueue.append(root.right)

    def insertinBST(self, node_val):
        if not self.data:
            self.data = node_val

        if node_val < self.data:
            if not self.left:
                self.left = BinaryTree(node_val)
                return
            else:
                self.left.insertinBST(node_val)
        else:
            if not self.right:
                self.right = BinaryTree(node_val)
                return
            else:
                self.right.insertinBST(node_val)


def depth(tree):
    pass


def traverse_quee(tree_queue, custDict, step=1):
    if not tree_queue:
        return custDict
    if len(tree_queue) < step:
        step = len(tree_queue)

    linked_list = LinkedList(tree_queue.popleft())
    for _ in range(step - 1):
        linked_list.add(tree_queue.popleft())

    key = list(custDict.keys())[-1] + 1
    custDict[key] = linked_list
    return traverse_quee(tree_queue, custDict, step * 2)


def treeToLinkedList(tree):
    customQueue = deque([tree])
    tree_queue = deque([tree.data])
    while customQueue:
        root = customQueue.popleft()
        if root.left:
            customQueue.append(root.left)
            tree_queue.append(root.left.data)
        if root.right:
            customQueue.append(root.right)
            tree_queue.append(root.right.data)

    custDict = {1: LinkedList(tree_queue.popleft())}
    return traverse_quee(tree_queue, custDict, step=2)


myBST = BinaryTree(20)
myBST.insertinBST(10)
myBST.insertinBST(5)
myBST.insertinBST(15)
myBST.insertinBST(25)
myBST.insertinBST(22)
myBST.insertinBST(30)

# vertical_view(myBST)
linked_lists_dict = treeToLinkedList(myBST)
print(linked_lists_dict)
