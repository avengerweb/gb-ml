# Переворачиваем число


# O(n) - где N - кол-во символов
# 1000 loops, best of 3: 9.27 usec per loop - 100100100100
# 1000 loops, best of 3: 4.29 usec per loop - 100100
# 1000 loops, best of 3: 2.25 usec per loop - 100
def calc(number):
    num_len = len(number)
    number = int(number)

    result_number = 0

    for i in range(0, num_len):
        result = number // 10 ** i % 10
        result_number += result * 10 ** (num_len - i - 1)

    return result_number


# O(1) - все остальное скрыто реализацией :)
# 1000 loops, best of 3: 0.587 usec per loop - 100
# 1000 loops, best of 3: 0.517 usec per loop - 100100
# 1000 loops, best of 3: 0.549 usec per loop - 100100100100
def calc2(number):
    return int(number[::-1])
