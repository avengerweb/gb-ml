# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MAX_LIMIT = 100
MIN_LIMIT = 0
array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

max_index = 0
min_index = 0

for idx, val in enumerate(array):
    if val > array[max_index]:
        max_index = idx

    if val < array[min_index]:
        min_index = idx

print(array)

if max_index != min_index:
    temp = array[max_index]
    array[max_index] = array[min_index]
    array[min_index] = temp


print(array)
