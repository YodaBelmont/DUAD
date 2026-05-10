class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_all(self):
        if self.head is None:
            print("THERE IS NO DATA")
            return

        current = self.head
        while current:
            print(current.data)
            current = current.next

    def insert_front(self, new_node):
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def insert_back(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def delete(self, node):
        if self.head is None:
            return
        if self.head.data == node.data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == node.data:
                current.next = current.next.next
                return
            current = current.next


node1 = Node("Michael Jackson")
node2 = Node("Twisted Fate")
node3 = Node("Emiliano")

list1 = LinkedList()

list1.insert_front(node1)
list1.insert_front(node3)
list1.insert_back(node2)

list1.print_all()
