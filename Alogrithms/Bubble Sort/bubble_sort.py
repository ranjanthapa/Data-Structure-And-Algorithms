from typing import List


def bubble_sort(list: List):
    size = len(list)
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp

    return list


list = [12, 11, 13, 67, 5, 30]
print(bubble_sort(list))
