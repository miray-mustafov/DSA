'''
Check if a binary tree is a Binary Search Tree.
'''


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def isValidBST(node, minn=float('-inf'), maxx=float('inf')):
    if not node:
        return True
    val = node.val
    if not minn < val < maxx:
        print(val, "is wrong positioned")
        return False

    if not isValidBST(node.left, minn, val):
        return False
    if not isValidBST(node.right, val, maxx):
        return False

    return True



# root1 = TreeNode(2)
# root1.left = TreeNode(1)
# root1.right = TreeNode(4)
#
# print(isValidBST(root1))

root2 = TreeNode(4)
root2.left = TreeNode(2)
root2.left.left = TreeNode(1)
root2.right = TreeNode(7)
root2.right.right = TreeNode(9)
root2.right.left = TreeNode(6)
# root2.right.left = TreeNode(2)  # Detect

print(isValidBST(root2))
