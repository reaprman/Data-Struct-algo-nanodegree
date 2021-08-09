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

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
    
    def __repr__(self):
        return str([v for v in self])


def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    rev_list = LinkedList()
    new_head = rev.head

    for value in linked_list:
        #if prepend function available rev.prepend(node.value)
        new_head = Node(value)
        new_head.next = rev_list.head
        rev_list.head = new_head
    
    return rev_list

    llist = LinkedList()
    for value in [4,2,5,1,-3,0]:
        llist.append(value)
    
    flipped = reverseList(llist)
    is_correct = list(flipped) == list([0.-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
    print("Pass" if is_correct else "Fail")