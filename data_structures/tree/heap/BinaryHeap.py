class BinaryHeap:
    def __init__(self, size):
        self.maxSize = size + 1
        self.customList = [None] * self.maxSize
        self.heapSize = 0  # maybe similar to last_used_index

    def peek(self):
        if self.customList[1]:
            return self.customList[1]
        print('Heap empty!')

    def levelOrderTraversal(self):
        for i in range(1, self.heapSize + 1):
            print(self.customList[i])

    def heapify(self, index, heap_type):  # index of the leaf that was lastly inserted
        parent_indx = index // 2
        if index <= 1:
            return
        if heap_type == "Min":
            if self.customList[index] < self.customList[parent_indx]:
                temp = self.customList[index]
                self.customList[index] = self.customList[parent_indx]
                self.customList[parent_indx] = temp
            self.heapify(parent_indx, heap_type)
        elif heap_type == "Max":
            if self.customList[index] > self.customList[parent_indx]:
                temp = self.customList[index]
                self.customList[index] = self.customList[parent_indx]
                self.customList[parent_indx] = temp
            self.heapify(parent_indx, heap_type)
        else:
            print("Wrong heap_type passed!")
            return

    def insertNode(self, node_value, heap_type):
        if self.heapSize + 1 == self.maxSize:
            print("Binary Heap is full!")
            return
        self.customList[self.heapSize + 1] = node_value
        self.heapSize += 1
        self.heapify(self.heapSize, heap_type)
        print(f"{node_value} inserted.")

    def heapifyExtract(self, index, heap_type):
        leftIndex = index * 2
        rightIndex = index * 2 + 1
        swapChild = 0

        if self.heapSize < leftIndex:
            return
        elif self.heapSize == leftIndex:
            if heap_type == "Min":
                if self.customList[index] > self.customList[leftIndex]:
                    temp = self.customList[index]
                    self.customList[index] = self.customList[leftIndex]
                    self.customList[leftIndex] = temp
                return
            else:
                if self.customList[index] < self.customList[leftIndex]:
                    temp = self.customList[index]
                    self.customList[index] = self.customList[leftIndex]
                    self.customList[leftIndex] = temp
                return

        else:
            if heap_type == "Min":
                if self.customList[leftIndex] < self.customList[rightIndex]:
                    swapChild = leftIndex
                else:
                    swapChild = rightIndex
                if self.customList[index] > self.customList[swapChild]:
                    temp = self.customList[index]
                    self.customList[index] = self.customList[swapChild]
                    self.customList[swapChild] = temp
            elif heap_type == "Max":
                if self.customList[leftIndex] > self.customList[rightIndex]:
                    swapChild = leftIndex
                else:
                    swapChild = rightIndex
                if self.customList[index] < self.customList[swapChild]:
                    temp = self.customList[index]
                    self.customList[index] = self.customList[swapChild]
                    self.customList[swapChild] = temp
            else:
                print("Wrong heap_type passed!")
                return
        self.heapifyExtract(swapChild, heap_type)

    def extractNode(self, heap_type):  # Only root_node can be extracted in BHeap
        if self.heapSize == 0:
            return  # Tree empty!

        extractedNode = self.customList[1]
        self.customList[1] = self.customList[self.heapSize]  # Swap lastly inserted node with root_node
        self.customList[self.heapSize] = None  # Delete last node (that had root_nodes value)
        self.heapSize -= 1
        self.heapifyExtract(1, heap_type)  # Reorder the tree to fullfill the heap rules
        return extractedNode

    def deleteHeap(self):
        self.customList = None


myHeap = BinaryHeap(10)
myHeap.insertNode(5, heap_type='Min')
myHeap.insertNode(8000, heap_type='Min')
myHeap.insertNode(10, heap_type='Min')
myHeap.insertNode(20, heap_type='Min')
myHeap.insertNode(30, heap_type='Min')
myHeap.insertNode(40, heap_type='Min')
myHeap.insertNode(50, heap_type='Min')
# myHeap.insertNode(60, heap_type='Min')
# myHeap.insertNode(70, heap_type='Min')

myHeap.levelOrderTraversal()
print()
# print('extracted: ' , myHeap.extractNode(heap_type='Max'))
myHeap.levelOrderTraversal()

