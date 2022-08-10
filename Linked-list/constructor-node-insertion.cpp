// Alternate method to declare the class in order to
//  to minimize the memory allocation work

#include <iostream>
using namespace std;

class node{
    public:
    int data;
    node* next;

    node(int value) // A constructor is called here
    {
        data = value; // it automatic assigns the value to the  data
        next = NULL;  // next pointer is pointed to NULL
    }
};
// func to insert a element at head position
void insertafter(node* head, int key, int val)
{
    node* n = new node(val);
    n->next = head;
    head = n;
}

// func to insert a element at a specified position