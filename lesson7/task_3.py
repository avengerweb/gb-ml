# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
# сложно, то используйте метод сортировки, который не рассматривался на уроках
import random


# То, что пришло в голову, O(n^2) и очень далеко от Median-of-medians Algorithm
def median(array):
    mid = (len(array) - 1) // 2
    for idx, val in enumerate(array):
        left = 0
        right = 0
        same = 0
        for idx2, val2 in enumerate(array):
            if val == val2:
                same += 1

            if val > val2:
                left += 1
            elif val < val2:
                right += 1

            if left > mid or right > mid:
                break

        if left + right + same == len(array) and left > 0 and right > 0 and left <= mid and right <= mid:
            return val


M = 20

array = [random.randint(-100, 100) for _ in range(2 * M + 1)]

print(array)
print(median(array))
print(sorted(array)[(len(array) - 1) // 2])


def test():
    counter = 0
    for _ in range(10000):
        array = [random.randint(-1000, 1000) for _ in range(2 * M + 1)]

        if sorted(array)[M] != median(array):
            print(array)
        else:
            counter += 1

    print(f'Success tested {counter} arrays')

# test()
