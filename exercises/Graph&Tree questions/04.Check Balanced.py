class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return self.value


def get_height(root):
    if root is None:
        return 0

    left_height = get_height(root.left)
    if left_height == -1: return -1

    right_height = get_height(root.right)
    if right_height == -1: return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1


def isBalanced(root):
    return get_height(root) > -1


N1 = Node("N1")
N2 = Node("N2")
N3 = Node("N3")
N4 = Node("N4")
N5 = Node("N5")
N6 = Node("N6")
N1.left = N2
# N1.right = N3
N2.left = N4
N2.right = N5
# N3.right = N6

print(isBalanced(N1))
