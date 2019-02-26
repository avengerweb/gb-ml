# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 30
MAX_LIMIT = 100
MIN_LIMIT = 0
array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

collector = {}

for val in array:
    collector[val] = collector.get(val, 0) + 1

max_index = None

for idx, val in collector.items():
    if max_index is None or val > collector[max_index]:
        max_index = idx

print(array)
print(max_index)

