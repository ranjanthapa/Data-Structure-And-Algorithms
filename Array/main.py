from typing import List


class MyArray:
    def __init__(self):
        self.length = 0
        self.data = []

    def get(self) -> List:
        return self.data

    @staticmethod
    def toDict(data: List[int]) -> dict:
        return {index: val for index, val in enumerate(data)}

    def push(self, item):
        self.data += [item]
        self.length += 1
        print(f"Data {item} pushed")

    def pop(self) -> None:
        if self.length == 0:
            print("Array is empty. Cannot perform pop operation.")
            return

        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        print(f"{last_item} popped from the array")

    def delete(self, index) -> None:
        try:
            del self.data[index]
            self.length -= 1
            print(f"{self.data[index]} delete")
        except IndexError:
            print("Index out of range")



newarray = MyArray()
newarray.push(10)
newarray.push(15)
newarray.push(16)
newarray.push(17)
newarray.push(18)
print()
newarray.pop()
newarray.delete(8)
print(newarray.length)
print(newarray.data)
print(MyArray.toDict(newarray.get()))
