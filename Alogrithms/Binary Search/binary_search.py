from typing import List
from utils import time_it


class SortingAlgorithms:

    @time_it
    def binary_search(self, number_list: List, number_to_find: int):
        left_index = 0
        right_index = len(number_list) - 1

        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            mid_value = number_list[mid_index]

            if mid_value == number_to_find:
                print(f"The {number_to_find} is at index {mid_index}")
                return mid_value
                break
            if mid_value < number_to_find:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1

        return -1

    @time_it
    def linear_search(self, number_list: List, number_to_find):
        for i in number_list:
            if i == number_to_find:
                return f"{number_to_find} is at index {number_list.index(number_to_find)}"
                break

        return -1

    def recursive_binary_search(self, number_list, number_to_find, left, right):
        if left > right:
            return -1

        mid_index = (right + left) // 2
        mid_value = number_list[mid_index]

        if mid_value == number_to_find:
            return f"{number_to_find} is at index {number_list.index(number_to_find)}"
        if mid_value < number_to_find:
            left = mid_index - 1
        else:
            right = mid_value + 1
        return self.recursive_binary_search(number_list, number_to_find, left, right)


if __name__ == '__main__':
    se = SortingAlgorithms()
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]
    number_to_find = 5
    se.binary_search(number_list, number_to_find)
