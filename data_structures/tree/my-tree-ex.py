from collections import deque, defaultdict

from data_structures.queue.QueueLinkedList import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return self.data



def preorder_traversal(tree_node):
    if not tree_node:
        return
    print(tree_node.data)
    preorder_traversal(tree_node.left_child)
    preorder_traversal(tree_node.right_child)


def inorder_traversal(tree_node):
    if not tree_node:
        return
    inorder_traversal(tree_node.left_child)
    print(tree_node.data)
    inorder_traversal(tree_node.right_child)


def postorder_traversal(tree_node):
    if not tree_node:
        return

    postorder_traversal(tree_node.left_child)
    postorder_traversal(tree_node.right_child)
    print(tree_node.data)


def levelorder_traversal_defaultdict(tree_node):
    level_nodes_dict = defaultdict(list)

    def dfs(node, level):
        if not node:
            return
        level_nodes_dict[level].append(node.data)
        dfs(node.left_child, level + 1)
        dfs(node.right_child, level + 1)
        a = 3

    dfs(tree_node, 0)
    [print([el for el in x]) for x in level_nodes_dict.values()]


def levelorder_traversal(tree_node):
    if not tree_node:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(tree_node)

        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.left_child is not None):
                customQueue.enqueue(root.value.left_child)

            if (root.value.right_child is not None):
                customQueue.enqueue(root.value.right_child)


def lvl_deque(tree_node):
    if not tree_node:
        return
    else:
        customQueue = deque([tree_node])

        while customQueue:
            root = customQueue.popleft()
            print(root.data)
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

print("\nPreorder traversal:")
preorder_traversal(my_binary_tree)

print("\nInorder traversal:")
inorder_traversal(my_binary_tree)

print("\nPostorder traversal:")
postorder_traversal(my_binary_tree)

print("\nDefaultdict Levelorder traversal:")
levelorder_traversal_defaultdict(my_binary_tree)

print("\nLevelorder traversal:")
levelorder_traversal(my_binary_tree)

print("\nDeque Levelorder traversal:")
lvl_deque(my_binary_tree)
