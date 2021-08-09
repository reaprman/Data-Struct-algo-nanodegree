class Node:
    def __init(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def to_list(self):
        ans = []
        node = self.head
        while node:
            ans.append(node.value)
            node = node.next
        return ans
    
    def prepend(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            node = Node(value)
            node.next = self.head
            self.head = node
        return

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return
    def search(self, value):
        if self.head == None:
            return -1
        else:
            node = self.head
            while node: # node != None
                if node.value == value:
                    return node
                node = node.next
        return -1

    def remove(self, value):
        node = self.head
        if node.value = value
        self.head = node.next
        return

        while node.next:
            nxt = node.next
            if nxt.value = value:
                node.next = nxt.next
                return
            node - node.next
        return

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        # TODO: Write function to pop here
        node = self.head
        out = node.value
        self.head = node.next # self.remove(out)
        return out

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """

        cnt = 0
        node = self.head
        while cnt != pos-1 and node.next:
            node = node.next
            cnt += 1
        nxt = node.next
        node.next = Node(value)
        node.next.next = nxt
        return

    def size(self):
        cnt = 0 
        node = self.head
        while node:
            cnt += 1
            node = node.next
        return cnt
    


LinkedList.prepend = prepend
LinkedList.append = append
LinkedList.search = search
LinkedList.remove = remove
LinkedList.pop = pop
LinkedList.insert = insert
LinkedList.size = size