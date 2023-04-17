from data_structures.tree.helpers import vertical_view

'''
Given a sorted (increasing order) array with unique integer elements, write
an algorithm to create a binary search tree with minimal height.
'''


class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def minimalTree(arr):
    if len(arr) == 3:
        return BSTNode(arr[1], BSTNode(arr[0]), BSTNode(arr[2]))
    elif len(arr) == 2:
        return BSTNode(arr[1], BSTNode(arr[0]))
    elif len(arr) == 1:
        return BSTNode(arr[0])

    mid_i = len(arr) // 2
    left_half_arr = arr[0:mid_i]
    right_half_arr = arr[mid_i + 1: len(arr)]

    root_node = BSTNode(arr[mid_i])
    root_node.left = minimalTree(left_half_arr)
    root_node.right = minimalTree(right_half_arr)

    return root_node


sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sortedArray2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_tree = minimalTree(sortedArray)
my_tree2 = minimalTree(sortedArray2)

vertical_view(my_tree)
# vertical_view(my_tree2)
