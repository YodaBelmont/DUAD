class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Double_Ended_Queue:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def print_queue(self):
        if self.front is None:
            print("NO DATA TO SHOW")
            return None
        node = self.front
        while node is not None:
            print(node)
            node = node.next

    def push_left(self, new_node):
        if self.front is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def push_right(self, new_node):
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def pop_left(self):
        if self.front is None:
            print("NO DATA TO DELETE")
            return None
        elif self.front == self.rear:
            node = self.front
            self.front = self.rear = None
            return node
        current = self.front
        self.front = self.front.next
        self.front.prev = None
        current.next = None
        return current

    def pop_right(self):
        if self.rear is None:
            print("THERE IS NO DATA TO DELETE")
            return None

        if self.rear == self.front:
            node = self.rear
            self.rear = self.front = None
            return node

        current = self.rear
        self.rear = self.rear.prev
        self.rear.next = None
        current.prev = None
        return current
