# A complete working Python3 program to
# demonstrate deletion in singly
# linked list with class

class Node:
    # constructor to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList():
    # func to initialize head
    def __init__(self):
        self.head = None
        
        
    # func to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
        
    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in linked list
        
    def deleteNode(self, key):
        # store head node
        temp = self.head
        
        # if head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
            
        # search for the keyy to be deleted, keep track of the
        # previous  node as we need to change prev.next
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
            
            
        # if key was not present in linked LinkedList
        if(temp == None):
            return
        
        # unlink the node from linked list 
        prev.next = temp.next
        temp = None
        
    # Utility func to print the linked linkedlist
    
    
    def printList(self):
        temp = self.head
        while(temp):
            print("%d" % (temp.data)),
            temp = temp.next
            
# driver code
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print("\nLinked List after Deletion of 1:")
llist.printList()
