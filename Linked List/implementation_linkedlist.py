class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, next=self.head)
        self.head = node

    def is_empty(self):
        return True if self.head == None else False

    def display(self):
        if self.is_empty():
            print("The linked list is empty")

        itr = self.head
        while itr:
            print(itr.data, end="-->")
            itr = itr.next
        print()

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, next=self.head)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)

    def insert_values(self, data_list: list):
        itr = self.head
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        itr = self.head
        count = 1
        while itr.next:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index == 0:
            self.head = self.head.next
            self.display()

        itr = self.head
        idx_count = 0
        while itr:
            if idx_count == index - 1:
                itr.next = itr.next.next
                self.display()
                break
            idx_count += 1
            itr = itr.next

    def insert_at(self, data, index):
        if index == 0:
            self.insert_at_begining(data)
        if index < 0 or index > self.get_length():
            raise Exception("Index invalid")

        itr = self.head
        idx_count = 0
        while itr.next:
            if idx_count == index - 1:
                node = Node(data, next=itr.next)
                itr.next = node
                break
            idx_count += 1
            itr = itr.next

    def insert_after_value(self, after_value, data_to):
        itr = self.head
        while itr:
            if itr.data == after_value:
                node = Node(data=data_to, next=itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        idx_count = 0
        while itr:
            if itr.data == data:
                self.remove_at(idx_count)
                break
            idx_count += 1
            itr = itr.next


ll = LinkedList()
ll.insert_at_end(30)
ll.insert_at_begining(20)
ll.insert_at_begining(25)
ll.insert_at_begining(22)
ll.display()
ll.insert_values([10, 11, 12, 32, 43])
ll.insert_at_begining(21)
ll.display()
ll.remove_at(2)
ll.insert_at(100, 7)
ll.insert_at("Hello", 6)

ll.insert_after_value("Hello", "world")
ll.display()
