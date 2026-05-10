class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def print_forward(self):
        if self.front is None:
            print("THERE IS NO DATA")
            return

        current = self.front
        while current:
            print(current.data)
            current = current.next

    def print_backward(self):
        if self.rear is None:
            print("THERE IS NO DATA")
            return

        current = self.rear
        while current:
            print(current.data)
            current = current.prev

    def prepend(self, new_node):
        if self.front is None:
            self.front = self.rear = new_node
            return

        new_node.next = self.front
        self.front.prev = new_node
        self.front = new_node

    def append(self, new_node):
        if self.rear is None:
            self.rear = self.front = new_node
            return

        new_node.prev = self.rear
        self.rear.next = new_node
        self.rear = new_node

    def delete(self, node):
        if self.front is None:
            return
        if self.front.data == node.data:
            self.front = self.front.next
            return
        current = self.front
        while current.next:
            if current.next.data == node.data:
                current.next = current.next.next
                return
            current = current.next


node1 = Node(1)
node2 = Node(5)
node3 = Node(9)
node4 = Node(11)
node5 = Node(0)

double_list = DoubleLinkedList()

double_list.append(node1)
double_list.append(node2)
double_list.append(node3)

double_list.prepend(node4)
double_list.prepend(node5)


double_list.print_forward()

double_list.print_backward()
