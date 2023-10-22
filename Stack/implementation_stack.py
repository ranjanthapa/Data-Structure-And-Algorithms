from typing import List, Union


class Stack:
    def __init__(self):
        self.stack: List = [None] * 4
        self.top = -1

    def isEmpty(self) -> bool:
        return self.top == -1

    def isFull(self) -> bool:
        return self.top == 3

    def push(self, item: Union[int, float]) -> None:
        if self.isFull():
            print("Stack is overflow")
        else:
            self.top += 1
            self.stack[self.top] = item

    def pushAtIndex(self, index: int, item: Union[int, float]):

        if not (0 <= index < 4):
            raise IndexError("Out of range")

        for i in range(self.top, index - 1, -1):
            self.stack[i + 1] = self.stack[i]

        self.stack[index] = item
        self.top += 1

    def pop(self):
        if self.isEmpty():
            print("THe stack is empty")
        else:
            self.stack[self.top] = None
            print("Item pop")

    def display(self) -> List:
        return self.stack

    def peek(self):
        if self.isEmpty():
            print("Stack is empty. Cannot peek.")
            return None
        else:
            return self.stack[self.top]


if __name__ == '__main__':
    stack = Stack()
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.pushAtIndex(2, 4000)
    print(stack.display())
    print(stack.peek())
