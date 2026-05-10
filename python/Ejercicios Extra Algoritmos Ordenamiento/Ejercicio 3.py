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


def sort_stack(stack_to_sort):
    stack_aux = Stack()
    while stack_to_sort.top is not None:
        original_node = stack_to_sort.pop()
        while stack_aux.top is not None and stack_aux.top.data > original_node.data:
            stack_to_sort.push(stack_aux.pop())

        stack_aux.push(original_node)


node2 = Node("Esteban")
node1 = Node("Dario")

stack = Stack(node1)

stack.push(node2)

stack.pop()

stack.print_stack()
stack.print_stack()
