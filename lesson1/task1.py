# Diagram: https://drive.google.com/file/d/1a9kCYcswKoV5ZW6rqUBEVIYrCGIcYt6d/view
# No validation required (good user)
number = int(input("Input three-digit number: "))

# We shouldn`t use arrays :(
digit1 = number // 100
digit2 = number // 10 % 10
digit3 = number % 10

dSum = digit1 + digit2 + digit3
dProduct = digit1 * digit2 * digit3

print("Sum of digit: %i\nProduct of digit: %i" % (dSum, dProduct))
