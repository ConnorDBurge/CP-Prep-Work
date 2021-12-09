class MyStack:

    def __init__(self, data):
        self.data = data

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

    def reversed(self):
        return self.data[::-1]


my_stack = MyStack([1, 2, 3, 4, 5])
my_stack.pop()
my_stack.push(6)
print(my_stack.reversed())


# Fibonacci iterative solution
def fibonacci_iterative(N):
    f, a, b = 0, 0, 1
    for _ in range(N - 1):
        f = a + b
        a = b
        b = f
    return f


def fibonacci_recursive(N):  # Fibonacci recursive solution
    if N < 2:
        return N
    return fibonacci_recursive(N-1) + fibonacci_recursive(N-2)


print(fibonacci_iterative(6))
print(fibonacci_recursive(6))
