class BinaryTreeList:
    def __init__(self, size):
        self.maxsize = size
        self.treelist = size * [None]
        self.last_used_idx = 0

    def visualize(self):
        print(self.treelist)

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

    def preOrderTraversal(self, index):
        if index > self.last_used_idx:
            return
        print(self.treelist[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self, index):
        if index > self.last_used_idx:
            return
        self.inOrderTraversal(index * 2)
        print(self.treelist[index])
        self.inOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self, index):
        if index > self.last_used_idx:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.treelist[index])

    def levelOrderTraversal(self, index):
        for i in range(index, self.last_used_idx + 1):
            print(self.treelist[i])

    def deleteNode(self, value):
        if self.last_used_idx == 0:
            return "There is not any node to delete"
        for i in range(1, self.last_used_idx + 1):
            if self.treelist[i] == value:
                self.treelist[i] = self.treelist[self.last_used_idx]
                self.treelist[self.last_used_idx] = None
                self.last_used_idx -= 1
                return "The node has been successfully deleted"

    def deleteBT(self):
        self.treelist = None
        return "The BT has been successfully deleted"


myBinaryTree = BinaryTreeList(8)

myBinaryTree.insert("Drinks")
myBinaryTree.insert("Hot")
myBinaryTree.insert("Cold")
myBinaryTree.insert("Coffee")
myBinaryTree.insert("Tea")
myBinaryTree.insert("Fanta")

coffee_indx = myBinaryTree.positionof('Coffee')
print(coffee_indx)

myBinaryTree.inOrderTraversal(1)

myBinaryTree.visualize()
