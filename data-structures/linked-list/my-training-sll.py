class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None  # no need its defaultly None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0

                while index < location - 1:
                    try:  # My bug solution(bug at singlyLinkedList.insertSLL(2, 3))
                        tempNode = tempNode.next
                        index += 1
                    except AttributeError:
                        tempNode = self.tail
                        break

                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    # Traverse Singly Linked List
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # Search for a node in Singly Linked List
    def searchSLL(self, nodeValue):
        if self.head is None:
            return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"

    def deleteNode(self, location):
        if self.head is None:
            print("linked list empty")

        elif self.head == self.tail and location in (0, -1):
            # if here we have only 1 node
            self.head = None
            self.tail = None

        elif location == 0:  # first head
            self.head = self.head.next
        elif location == -1:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next

            self.tail = current_node
            self.tail.next = None
        else:
            index = 0
            current_node = self.head
            try:
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                current_node.next = current_node.next.next
            except AttributeError:
                print('invalid location!')

    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 3)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(9, -1)

print([node.value for node in singlyLinkedList])

singlyLinkedList.deleteNode(-1)

print([node.value for node in singlyLinkedList])

singlyLinkedList.deleteEntireSLL()

print([node.value for node in singlyLinkedList])

