# node class
class Node:
    # functiion to intialisze the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # initialise
        # next as null
        
# linkedlist class
class LinkedList:
    # func to intialisze the linked object
    # list object
    def __init__(self):
        self.head = None
    
    # Python program for traversal of a linked list
    # This func prints contents of linked list
    # starting from head   
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next   
#  simple linked list with 3 nodes

# code execution starts here
if __name__ == '__main__':
    # star with the empty list
    llist = LinkedList()
    
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    """
    Three node have been created 
    we have references to thes three blocks as head,
    second and third
    
    llist.head        second              third
         |                |                  |
         |                |              p    |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    
    """
    
    llist.head.next = second; # link first node with second
    
    '''
     Now next of first Node refers to second.  So they
    both are linked.
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+ 
    
    '''
    
    second.next =third; # link second node with  the third node
    
    '''
    Now next of second Node refers to third.  So all three
    nodes are linked.
  
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+ 
    
    
    '''
    
    print(llist)
    print(llist.head)
    print(second)    
    print(third)
    
    llist.printList()

    