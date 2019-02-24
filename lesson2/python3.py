number = input("Enter number: ")

num_len = len(number)
number = int(number)

resultNumber2 = 0

for i in range(0, num_len):
    result = number // 10 ** i % 10
    resultNumber2 += result * 10 ** (num_len - i - 1)

print(resultNumber2)
