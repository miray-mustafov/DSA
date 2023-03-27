class BinaryTreeList:
    def __init__(self, size):
        self.maxsize = size
        self.treelist = size * [None]
        self.last_used_idx = 0

    def insert(self, val):
        if self.last_used_idx + 1 == self.maxsize:
            return print("Tree Full!")
        self.treelist[self.last_used_idx + 1] = val
        self.last_used_idx += 1
        return print(f"{val} inserted at the first empty position!")

    def positionof(self, val):  # search for node
        try:
            position = self.treelist.index(val)
        except ValueError:
            return print('Not found!')
        return position

    def visualize(self):
        print(self.treelist)


myBinaryTree = BinaryTreeList(8)
myBinaryTree.insert("Drinks")
myBinaryTree.insert("Hot")
myBinaryTree.insert("Cold")
myBinaryTree.insert("Coffee")

coffee = myBinaryTree.positionof('Coffee')

myBinaryTree.visualize()
