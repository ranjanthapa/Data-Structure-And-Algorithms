from typing import List


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_value_at_first(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertValueList(self, data_list: List):
        for data in data_list:
            node = Node(data, self.head)
            self.head = node

    def insertValueEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
        itr = self.head
        while itr.next:
            itr = itr.next
            print(itr)
        itr.next = Node(data, None)

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next

        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        print(f"The length of node is {count}")
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_value_at_first(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertValueList(["Messi", "Neymar", "Suarez", "Xavi"])

    ll.display()
    ll.remove_at(1)
    ll.insert_at(2, "Ranjan")
    ll.display()

    ll.get_length()
