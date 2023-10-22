class Node:
    def __init__(self, data=None, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, previous=None, next=self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.is_empty():
            self.insert_at_begining(data)
            return  # Return to exit the function after inserting at the beginning

        itr = self.head
        while itr:
            if itr.next == None:
                node = Node(data, previous=itr, next=None)
                itr.next = node
                break
            itr = itr.next

    def is_empty(self):
        return True if self.head == None else False

    def display(self):
        if not self.is_empty():
            itr = self.head
            while itr:
                print(itr.data, end="-->")
                itr = itr.next

    def display_reversely(self):
        if not self.is_empty():
            itr = self.head
            while itr:
                itr = itr.next
            while itr:
                print(itr.data, end="-->")
                itr = itr.previous


dll = DoublyLinkedList()
dll.insert_at_begining(42)
dll.insert_at_end(20)
dll.insert_at_begining(40)
dll.display()
dll.display_reversely()
