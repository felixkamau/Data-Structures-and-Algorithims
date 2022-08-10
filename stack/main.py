# python implementation of stack
# using list

from traceback import print_stack


stack = []

# append() func to push
# element in the stack

stack.append('mark')
stack.append('felix')
stack.append('julie')
stack.append('henry')
stack.append('jeremy')

print('INitial stack')
print(stack)


# pop() func to pop
# element from stack in
# LIFO order

print('\nElements after elements are popped: ')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped: ')
print(stack)
print(stack)
