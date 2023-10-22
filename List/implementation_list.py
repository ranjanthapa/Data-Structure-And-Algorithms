from typing import List


class ImplementationList:
    def __init__(self):
        self.list: List = []

    def insert(self, data):
        self.list.append(data)

    def replace_item(self, index: int, data):
        self.list[index] = data

    def delete_item(self, index: int):
        del self.list[index]

    def insert_at(self, index: int, data):
        self.list.insert(index, data)
