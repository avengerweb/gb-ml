import sys
import random
import inspect


def show_size(x, level=0):
    name = ''
    if level == 0:
        name = f'Variable: "{str([k for k, v in inspect.currentframe().f_back.f_locals.items() if v is x][0])}", '

    final_size = 0
    size = sys.getsizeof(x)
    print('\t' * level, name, f'type={type(x)}, size={size}, obj={x}', sep='')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                final_size += show_size(key, level + 1)
                final_size += show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                final_size += show_size(item, level + 1)

    final_size += size
    show_size.app_allocated_size += size

    if size != final_size:
        print('\t' * level, f'Allocated size: {final_size}\n', sep='')

    return final_size


show_size.app_allocated_size = 0


# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8,
# 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
# начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
def l3_p2():
    SIZE = 10
    MAX_LIMIT = 100
    MIN_LIMIT = 0
    array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
    result = []

    for idx, val in enumerate(array):
        if val % 2 == 0:
            result.append(idx)

    print(array)
    print(result)
    show_size(array)
    show_size(result)
    show_size(SIZE)
    show_size(MAX_LIMIT)
    show_size(MAX_LIMIT)


# 4. Определить, какое число в массиве встречается чаще всего.
def l3_p4():
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
    show_size(array)
    show_size(max_index)
    show_size(collector)
    show_size(SIZE)
    show_size(MAX_LIMIT)
    show_size(MIN_LIMIT)


l3_p2()

print("*" * 140, "\n")

l3_p4()

print('\n' * 2, f'App was allocated: {show_size.app_allocated_size}', sep='')

