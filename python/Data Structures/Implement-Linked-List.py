class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(2)
print(head.value)
print(head.next)

def create_linked_list(input_list):
    """ Function to create a linked list
    @param input_list: a list of integers
    @return: head node of linked list 
    """
    head = None
    for item in input_list:
        if head == None:
            head = Node(item)
            current = head
        else:
            current.next = Node(item)
            current = current.next
    
    return head

def print_linked_list(head):
    current = head
    while current.next: 
        print(current.value)
        current = curren.next
    print(current.value)

def create_linked_list_better(input_list):
    head = None
    tail = None

    for item in input_list:
        if head == None:
            head = Node(item)
            tail = head
        else:
            tail.next = Node(item)
            tail = tail.next
    return head