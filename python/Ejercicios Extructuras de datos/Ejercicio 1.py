class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, top=None):
        self.top = top

    def print_stack(self):
        if self.top is None:
            print("EMPTY STACK")
            return

        current = self.top
        while current is not None:
            print(current.data)
            current = current.next

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        node = self.top
        self.top = self.top.next
        return node.data


node2 = Node("Esteban")
node1 = Node("Dario")

stack = Stack(node1)

stack.push(node2)

stack.pop()

stack.print_stack()
stack.print_stack()
