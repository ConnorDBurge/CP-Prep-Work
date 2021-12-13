from bstnode import BSTNode


class BST:
    def __init__(self):
        self.root = None

    def print(self):
        if self.root is not None:
            self._print(self.root)

    def _print(self, current):  # in-order traversal
        if current is not None:
            self._print(current.left)
            print(f'{current.data}')
            self._print(current.right)

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current):
        if data < current.data:
            if current.left is None:
                current.left = BSTNode(data)
                current.left.parent = current
            else:
                self._insert(data, current.left)
        elif data > current.data:
            if current.right is None:
                current.right = BSTNode(data)
                current.right.parent = current
            else:
                self._insert(data, current.right)
        else:
            print('Value already in tree')

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current, height):
        if current is None:
            return height
        else:
            left_height = self._height(current.left, height + 1)
            right_height = self._height(current.right, height + 1)
            return max(left_height, right_height)

    def find(self, data):
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, current):
        if data == current.data:
            return current
        elif data < current.data:
            if current.left is None:
                return None
            else:
                return self._find(data, current.left)
        elif data > current.data:
            if current.right is None:
                return None
            else:
                return self._find(data, current.right)

    def delete_value(self, data):
        return self.delete_node(self.find(data))

    def delete_node(self, node):
        def min_value_node(n):
            current = n
            while current.left is not None:
                current = current.left
            return current

        def num_children(n):
            num_children = 0
            if n.left is not None:
                num_children += 1
            if n.right is not None:
                num_children += 1
            return num_children

        node_parent = node.parent
        node_children = num_children(node)

        # CASE 1 (node has no children)
        if node_children == 0:
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None

        # CASE 2 (node has a single child)
        if node_children == 1:
            if node.left is not None:
                child = node.left
            else:
                child = node.right

            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child

            child.parent = node_parent

        # CASE 3 (node has two children)
        if node_children == 2:
            successor = min_value_node(node.right)
            node.data = successor.data
            self.delete_node(successor)

    def search(self, data):
        if self.root is not None:
            return self._search(data, self.root)
        else:
            return False

    def _search(self, data, current):
        if data == current.data:
            return True
        elif data < current.data:
            if current.left is None:
                return False
            else:
                return self._search(data, current.left)
        elif data > current.data:
            if current.right is None:
                return False
            else:
                return self._search(data, current.right)


def fill_tree(tree, elements=10, max=100):
    from random import randint
    for _ in range(elements):
        cur = randint(0, max)
        tree.insert(cur)


if __name__ == '__main__':
    tree = BST()
    tree.insert(5)
    tree.insert(4)
    tree.insert(6)
    tree.insert(10)
    tree.insert(9)
    tree.insert(11)
    tree.print()
    tree.delete_value(6)
    tree.print()
