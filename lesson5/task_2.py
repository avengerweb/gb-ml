# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как
# [‘A’,‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
import random

numbers = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

MOD = 16

num_to_hex = dict(zip(numbers.values(), numbers.keys()))


def hex_single_sum(num1, num2):
    n1 = numbers[num1]
    n2 = numbers[num2]
    result = deque()
    num = n1 + n2

    while num >= MOD:
        result.append(num_to_hex[num % MOD])
        num = num // MOD

    result.append(num_to_hex[num % MOD])

    result.reverse()

    return result


def hex_sum(num1, num2):
    max_len = max(len(num1), len(num2))
    min_len = min(len(num1), len(num2))
    diff = max_len - min_len
    if len(num2) > len(num1):
        temp = num1
        num1 = num2
        num2 = temp

    result = deque()
    prev = deque()
    for i in range(max_len - 1, -1, -1):
        n1 = num1[i]
        i_2 = i - diff
        if len(prev) != 0:
            prev = hex_single_sum(n1, prev.pop())
            if len(prev) == 2:
                prev.pop()  # is 0
                result.append(num2[i_2] if i_2 > - 1 else '0')
                if i == 0:
                    prev.reverse()
                    result.extend(prev)
                continue
            n1 = prev.pop()

        prev = hex_single_sum(n1, num2[i_2] if i_2 > - 1 else '0')

        if i != 0:
            result.append(prev.pop())
        else:
            prev.reverse()
            result.extend(prev)

    result.reverse()
    return result


def test():
    for i in range(1000, 100000):
        n1 = hex(i).upper().replace("0X", "")
        n2_num = random.randint(0, 1000000)
        n2 = hex(n2_num).upper().replace("0X", "")
        s = hex_sum(n1, n2)
        res = int(''.join(s), 16)

        if n2_num + i != res:
            print(n1, n2, s, res, hex(n2_num + i))


num_list_1 = list(input("Enter first hex num: "))
num_list_2 = list(input("Enter second hex num: "))

print(f"{num_list_1} + {num_list_2} = {list(hex_sum(num_list_1, num_list_2))}")
