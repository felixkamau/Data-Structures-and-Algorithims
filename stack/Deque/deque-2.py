# demonstrate stack implementation
# using collections.deque

from collections import deque

stack = deque()

# append function to push
# element in the stack

stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
stack.append('e')
stack.append('f')
stack.append('g')
stack.append('h')
stack.append('i')
stack.append('j')

print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('/nElements popped from stack: ')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped: ')
print(stack)