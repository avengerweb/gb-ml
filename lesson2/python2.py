number = input("Enter number: ")

num_len = len(number)
number = int(number)

odd = 0
even = 0

for i in range(num_len, 0, -1):
    result = number // 10 ** (i - 1) % 10
    if result % 2 == 0:
        even += result
    else:
        odd += result

print(f"Odd sum: {odd}, Even sum: {even}")

