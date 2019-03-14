# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы
import random


def merge_sort(array):

    if len(array) == 1:
        return array

    middle = len(array) // 2

    left = array[:middle]
    right = array[middle:]

    merge_sort(left)
    merge_sort(right)

    i = 0
    left_i = 0
    right_i = 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            array[i] = left[left_i]
            left_i += 1
        else:
            array[i] = right[right_i]
            right_i += 1
        i += 1

    while left_i < len(left):
        array[i] = left[left_i]
        left_i += 1
        i += 1

    while right_i < len(right):
        array[i] = right[right_i]
        right_i += 1
        i += 1

    return array


array = [random.randint(0, 50) for _ in range(10)]
print(array)
merge_sort(array)
print(array)
