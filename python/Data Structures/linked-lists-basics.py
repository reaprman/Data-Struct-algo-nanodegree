class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(1)
head.next = Node(2)

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            current = self.head
            while current != None:
                current = current.next
            current = Node(value)
        
        return 

    def to_list(self):
        arr = []
        node = self.head

        while node:
            arr.append(node.value)
            node = node.next

        return arr

lnked_list = LinkedList()
lnked_list.append(1)
lnked_list.append(2)
lnked_list.append(4)

node = linked_list.head
while(node):
    print(node.value)
    node = node.next


class DoubleNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        if self.tail == None:
            self.head = DoubleNode(value)
            self.tail = self.head
        else:
            tail = self.tail
            tail.next = DoubleNode(value)
            tail.next.prev = tail
            self.tail = tail.next

        return