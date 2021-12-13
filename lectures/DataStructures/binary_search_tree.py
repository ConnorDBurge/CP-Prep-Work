from BSTNode import BSTNode


class BinarySearchTree:
    root = None

    def __init__(self, elements):
        self.root = BSTNode(elements[0])
        for i in range(1, len(elements)):
            self.append(elements[i])

    def append(self, data, root_node=None):
        if root_node is None:
            root_node = self.root
        if data == root_node.data:  # data already exist
            return
        if data < root_node.data:  # go to left
            if root_node.left is not None:
                self.append(data, root_node.left)  # call add child again
            else:  # if it is None, add new left child
                root_node.left = BSTNode(data)
        if data > root_node.data:  # go to right
            if root_node.right is not None:
                self.append(data, root_node.right)  # call add child again
            else:  # if it is None, add new right child
                root_node.right = BSTNode(data)

    def in_order_traversal(self, root_node=None):
        elements = []
        if root_node is None:
            root_node = self.root
        if root_node is not None:
            if root_node.left is not None:  # visit left tree first
                elements += self.in_order_traversal(root_node.left)
            elements.append(root_node.data)  # visit root_node node
            if root_node.right is not None:  # visit right tree second
                elements += self.in_order_traversal(root_node.right)
            return elements

    def post_order_traversal(self, root_node=None):
        elements = []
        if root_node is None:
            root_node = self.root
        if root_node is not None:
            if root_node.left is not None:  # visit left tree first
                elements += self.in_order_traversal(root_node.left)
            if root_node.right is not None:  # visit right tree second
                elements += self.in_order_traversal(root_node.right)
            elements.append(root_node.data)  # visit root_node node
            return elements

    def pre_order_traversal(self, root_node=None):
        elements = []
        if root_node is None:
            root_node = self.root
        if root_node is not None:
            elements.append(root_node.data)  # visit root_node node
            if root_node.left is not None:  # visit left tree first
                elements += self.in_order_traversal(root_node.left)
            if root_node.right is not None:  # visit right tree second
                elements += self.in_order_traversal(root_node.right)
            return elements

    def search(self, data, root_node=None):
        if root_node is None:
            root_node = self.root
        if root_node.data == data:
            return True
        if data < root_node.data:  # might be in left subtree
            if root_node.left is not None:
                return self.search(data, root_node.left)
            else:
                return False
        if data > root_node.data:  # might be in right subtree
            if root_node.right is not None:
                return self.search(data, root_node.right)
            else:
                return False


if __name__ == '__main__':
    import random
    numbers = random.sample(range(0, 30), 15)
    numbers1 = [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]
    numbers_tree = BinarySearchTree(numbers1)
    print('In-Order: ', numbers_tree.in_order_traversal())
    print('Pre-Order: ', numbers_tree.pre_order_traversal())
    print('Post-Order: ', numbers_tree.post_order_traversal())
