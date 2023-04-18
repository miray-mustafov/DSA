from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)


def preorderIterative_helper(root, n1, n2):
    if root is None: return

    stack = deque()
    stack.append(root)
    curr = root

    while stack:
        if curr:
            if curr.value in [n1, n2]:
                return curr.value

            if curr.right:
                stack.append(curr.right)

            curr = curr.left
        else:
            curr = stack.pop()


def preorderIterative(root, n1, n2):
    if root is None: return

    stack = deque()
    stack.append(root)
    curr = root

    while stack:
        if curr:
            t1 = preorderIterative_helper(curr.left, n1, n2)
            t2 = preorderIterative_helper(curr.right, n1, n2)
            if t1 == n1 and t2 == n2 or t1 == n2 and t2 == n1:
                return curr

            if curr.right:
                stack.append(curr.right)

            curr = curr.left
        else:
            curr = stack.pop()
    return False


# def preorder_traversal(node, searched):
#     if not node:
#         return
#     if node.value in searched:
#         return node.value
#     preorder_traversal(node.left, searched)
#     preorder_traversal(node.right, searched)
#
#
# def findFirstCommonAncestor(n1, n2, node):
#     if not node:
#         return
#
#     preorder_traversal(node, [n1, n2])
#     findFirstCommonAncestor(n1, n2, node.left)
#     findFirstCommonAncestor(n1, n2, node.right)


my_tree = Node(55)
my_tree.right = Node(77)

l_subtr = Node(44)
l_subtr.left = Node(22)
l_subtr.left.left = Node(35)
l_subtr.left.right = Node(88)
l_subtr.left.right.left = Node(54)

l_subtr.right = Node(99)
l_subtr.right.right = Node(95)
l_subtr.right.left = Node(90)
l_subtr.right.left.right = Node(33)

my_tree.left = l_subtr
n1 = 88
n2 = 33
print(preorderIterative(my_tree, n1, n2))
# print(findFirstCommonAncestor(88, 33, node=my_tree))
