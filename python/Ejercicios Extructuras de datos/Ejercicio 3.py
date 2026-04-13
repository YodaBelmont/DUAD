class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Binary_Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            self.recursive_insert(current, new_node)

    def print_tree(self):
        self.print_in_Order(self.root)

    def print_in_Order(self, node):
        if node:
            self.print_in_Order(node.left)
            print(node.data)
            self.print_in_Order(node.right)

    def recursive_insert(self, current, new_node):
        if new_node.data <= current.data:
            if current.left is None:
                current.left = new_node
            else:
                self.recursive_insert(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self.recursive_insert(current.right, new_node)


node1 = Node(3)
node2 = Node(5)
node3 = Node(10)
node4 = Node(1)
node5 = Node(9)


tree = Binary_Tree()

tree.insert(node1)
tree.insert(node2)
tree.insert(node3)
tree.insert(node4)
tree.insert(node5)

tree.print_tree()
