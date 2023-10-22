class CircularQueue:
    def __init__(self, size: int):
        self.size = size
        self.queue = [None] * size
        self.rear = self.front = -1

    def is_full(self) -> bool:
        return True if (self.rear + 1) % self.size == self.front else False

    def is_empty(self) -> bool:
        return True if self.rear == -1 else False

    def enqueue(self, data: int):
        if not self.is_full():
            if self.front == -1:
                self.front += 1
                self.rear += 1
                self.queue[self.rear] = data
            else:
                self.rear = (self.rear + 1) % self.size
                self.queue[self.rear] = data
        else:
            print(f"The queue is full")

    def dequeue(self):
        if not self.is_empty():
            if self.rear == self.front:
                temp = self.queue[self.front]
                self.rear = -1
                self.front = -1
                print(f"\n{temp} is removed from the queue")
            else:
                temp = self.queue[self.front]
                self.front = (self.front + 1) % self.size
                print(f"\n{temp} is removed from the queue")

        else:
            print("The queue is empty")

    def display_cqueue(self):
        if not self.is_empty():
            if self.rear >= self.front:
                for i in range(self.front, self.rear + 1):
                    print(self.queue[i], end=" ")

            else:
                for i in range(self.front, self.rear):
                    print(self.queue[i], end="")


obj = CircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.display_cqueue()

obj.dequeue()
print("\nAfter removing an element from the queue")
obj.display_cqueue()
