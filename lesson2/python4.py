count = int(input("Enter quantity of numbers: "))

rangeSum = 0

for i in range(0, count):
    rangeSum += (1 if i % 2 == 0 else -1) / (2 ** i)

print(rangeSum)
