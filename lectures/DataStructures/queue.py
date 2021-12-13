from node import Node
# First in First Out (FIFO)


class Queue:
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

    def dequeue(self):
        data = self.head.next.data
        self.head.next = self.head.next.next
        self.length -= 1
        return data


my_queue = Queue()
my_queue.push(0)
my_queue.push(1)
my_queue.push(2)
my_queue.push(3)
my_queue.push(4)
my_queue.push(5)
print(my_queue)
print(my_queue.dequeue())
print(my_queue)
print(my_queue.dequeue())
print(my_queue)
print(my_queue.dequeue())
print(my_queue)
