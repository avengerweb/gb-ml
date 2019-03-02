# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# ТЗ, так себе... Понимаю под "максимальный отрицательный" самое близкое к 0 отрицательное число. Иначе - минимальное

import random

SIZE = 10
MAX_LIMIT = 100
MIN_LIMIT = -100
array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

max_index = None

for idx, val in enumerate(array):
    if val > 0:
        continue

    if max_index is None or val > array[max_index]:
        max_index = idx

print(array)

if max_index is None:
    print("No negative numbers in array")
else:
    print(f"Position: {max_index}, value: {array[max_index]}")
