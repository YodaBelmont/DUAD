class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def print_queue(self):
        if self.front is None:
            print("THERE IS NO DATA")
            return
        current = self.front
        while current is not None:
            print(current.data)
            current = current.next

    def enqueue(self, new_node):
        if self.rear is None:
            self.rear = self.front = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("THERE IS NO DATA TO DELETE")
            return
        elif self.front == self.rear:
            node = self.front
            self.rear = self.front = None
            return node.data

        node = self.front
        self.front = self.front.next
        return node.data


node1 = Node("Esteban")
node2 = Node("Juancho")
node3 = Node("Duki")
node4 = Node("Azazel")
node5 = Node("Gabriel")

queue1 = Queue()

queue1.enqueue(node1)
queue1.enqueue(node2)
queue1.enqueue(node3)
queue1.enqueue(node4)
queue1.enqueue(node5)

queue1.print_queue()

queue1.dequeue()
queue1.dequeue()

queue1.print_queue()
