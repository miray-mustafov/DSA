class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CurricularSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return print(f"LL created with value {nodeValue}")

    def insertCSLL(self, value, location):
        def new_tail():
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head

        if self.head is None and location is 0:
            self.createCSLL(value)
            return
        elif self.head is None:
            return print("create the ll first")

        newNode = Node(value)
        if location == 0:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head
        elif location == -1:  # insert in last
            new_tail()
        else:
            currentLocation = 0
            previousNode = self.head
            while currentLocation < location - 1:
                previousNode = previousNode.next
                if previousNode.next == self.head:
                    return print("location outside of linked list")
                currentLocation += 1

            newNode.next = previousNode.next
            previousNode.next = newNode


myCSLL = CurricularSLL()
# myCSLL.createCSLL(9)
myCSLL.insertCSLL(4, 1)

# myCSLL.insertCSLL(4, -1)
# myCSLL.insertCSLL(15, -1)
# myCSLL.insertCSLL(22, 0)
# print([node.value for node in myCSLL])
# myCSLL.insertCSLL(99, 5)
# circularSLL.insertCSLL(3, 1)

print([node.value for node in myCSLL])

try:
    print(f"next of tail: {myCSLL.tail.next.value}")
except AttributeError:
    print('Finish')

