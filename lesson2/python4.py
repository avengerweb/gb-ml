count = int(input("Enter quantity of numbers: "))

range_sum = 0

for i in range(0, count):
    range_sum += (1 if i % 2 == 0 else -1) / (2 ** i)

print(range_sum)
