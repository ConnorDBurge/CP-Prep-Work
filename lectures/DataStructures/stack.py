from node import Node
import re
# Last in First Out (LIFO)


class Stack:
    def __init__(self):
        self.head = Node()
        self.length = 0

    def __str__(self):
        string = ''
        current = self.head.next
        while current is not None:
            string += f'{current.data} '
            current = current.next
        return string

    def push(self, data):
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.length += 1

    def pop(self):
        current = self.head
        while current.next is not None:
            prev_node = current
            current = current.next
        data = current.data  # save data to return
        prev_node.next = current.next
        self.length -= 1
        return data


my_stack = Stack()
my_stack.push(0)
print(my_stack)
my_stack.push(1)
print(my_stack)
my_stack.push(2)
print(my_stack)
my_stack.push(3)
print(my_stack)
my_stack.push(4)
print(my_stack)
my_stack.push(5)
print(my_stack)
my_stack.pop()
print(my_stack)
my_stack.pop()
print(my_stack)
my_stack.pop()
print(my_stack)
my_stack.pop()
print(my_stack)
my_stack.pop()
print(my_stack)
