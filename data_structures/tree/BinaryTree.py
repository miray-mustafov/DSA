from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return "n" + self.data


def searchinBT(tree_node, node_data):
    # its level order traversal
    if not tree_node:
        return
    else:
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
    if not tree_node:
        return
    else:
        customQueue = deque([tree_node])

        while customQueue:
            cur_node = customQueue.popleft()
            if cur_node.left_child:
                customQueue.append(cur_node.left_child)
            else:
                cur_node.left_child = new_node
                return f"{new_node} left child added"

            if cur_node.right_child:
                customQueue.append(cur_node.right_child)
            else:
                cur_node.right_child = new_node
                return f"{new_node} right child added"


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

print(
insert1by1BT(my_binary_tree, Node("New Left")),
insert1by1BT(my_binary_tree, Node("New Right")),

