# Diagram: https://drive.google.com/file/d/1J9pKSaA9HJgv_tliw6Q6Ip_kT7iTHPa-/view?usp=sharing
import random

print("Random INTEGER (any integer number)")
range_start = int(input("Range start: "))
range_end = int(input("Range end: "))

# inclusive
range_end += 1

result = random.randrange(range_start, range_end)

print("Result: %i" % result)

print("Random FLOAT (any float number)")

range_start = float(input("Range start: "))
range_end = float(input("Range end: "))

result = random.triangular(range_start, range_end)

print("Result: %f" % result)

print("Random LETTER (a-z)")

range_start = input("Range start: ")
range_end = input("Range end: ")

# convert to int
range_start = ord(range_start)
range_end = ord(range_end) + 1

letter = chr(random.randrange(range_start, range_end))

print("Result: %s" % letter)
