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


myHeap = BinaryHeap(5)
myHeap.insertNode(4,heap_type='Max')
myHeap.insertNode(2,heap_type='Max')
myHeap.insertNode(1,heap_type='Max')
myHeap.insertNode(5,hea p_type='Max')
myHeap.levelOrderTraversal()

