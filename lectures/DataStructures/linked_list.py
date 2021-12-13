from node import Node


class SLinkedList:
    def __init__(self):
        self.head = Node()
        self.length = 0

    def __str__(self):
        string = ''
        current = self.head.next
        while current is not None:
            string += f'{current.data} -> '
            current = current.next
        return string

    def push(self, data):
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.length += 1

    def length(self):
        return self.length

    def display(self):
        elements = []
        current = self.head
        while current.next is not None:
            current = current.next
            elements.append(current.data)
        print(elements)

    def get(self, index):
        if index >= self.length:
            raise ValueError("Index out of bounds")
        c_index = 0
        current = self.head
        while True:
            current = current.next
            if c_index == index:
                return current.data
            else:
                c_index += 1

    def remove(self, index):
        if index >= self.length:
            raise ValueError("Index out of bounds")
        c_index = 0
        current = self.head
        while True:
            prev_node = current
            current = current.next
            if c_index == index:
                prev_node.next = current.next
                self.length -= 1
                return
            else:
                c_index += 1


my_list = SLinkedList()
my_list.push(0)
my_list.push(1)
my_list.push(2)
my_list.push(3)
my_list.push(4)
my_list.push(5)
my_list.remove(4)
print(my_list)
