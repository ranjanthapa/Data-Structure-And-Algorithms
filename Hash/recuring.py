from typing import List


# This approach has time complexity of O(n^2)
class RecurringArray:
    def firstRecuring(self, arry: List) -> int:
        new_list = []
        for i in range(len(arry) - 1):
            temp = arry[i]
            if temp == arry[i + 1]:
                return temp
                break
            else:
                new_list.append(temp)
                temp = arry[i + 1]
                for j in new_list:
                    if temp == j:
                        return temp
                        break


# This approach has time complexity of O(n)
class RecurringArray2:
    def __init__(self):
        self.hashArray = {}

    def firstRecuring(self, array: List):

        for i in array:
            if self.hashArray.get(i) == i:
                return self.hashArray[i]
            else:
                self.hashArray[i] = i


b = RecurringArray2()
print(b.firstRecuring([2, 5, 5, 2, 1, 5]))
print(b.hashArray)
