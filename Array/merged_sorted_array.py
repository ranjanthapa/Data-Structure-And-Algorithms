from typing import List


class MergeSortedArray:
    def mergeArray(self, **kwargs) -> List[int]:
        new_array = []
        for key, value in kwargs.items():
            new_array.extend(value)

        return self.mergeSort(new_array)

    def mergeSort(self, array) -> List[int]:
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left = self.mergeSort(array[:mid])
        print(left)

        right = self.mergeSort(array[mid:])
        print(right)

        return self.merge(left, right)

    def merge(self, left, right) -> List[int]:
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged


if __name__ == "__main__":
    arraymerge = MergeSortedArray()
    print(arraymerge.mergeArray(array1=[1, 2, 3, 45, 5, 3], array2=[4, 2, 52, 2, 5, 2]))
