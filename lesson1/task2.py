# Diagram: https://drive.google.com/file/d/1eD3POUGP-JkVEhTH1uQJEKQ2w5jMSRKY/view?usp=sharing
# 5
n1 = 0b101
# 6
n2 = 0b110

print("Числа: %s, %s (%i, %i)" % (bin(n1), bin(n2), n1, n2))

bit_or = n1 | n2
bit_and = n1 & n2
bit_xor = n1 ^ n2
left_shift = n1 << 2
right_shift = n1 >> 2

# OR - если один из битовов равен еденице, то результирующий будет равен 1
# 1 0 1
#  OR
# 1 1 0
# =
# 1 1 1
print("OR: %s (%i)" % (bin(bit_or), bit_or))

# AND - если оба бита равны еденице, то результирующий будет равен 1, во всех других случиях = 0
# 1 0 1
#  OR
# 1 1 0
# =
# 1 1 1
print("AND: %s (%i)" % (bin(bit_and), bit_and))

# xor - если оба бита равны, то результирующий будет равен 0, если нет, то 1
# 1 0 1
#  OR
# 1 1 0
# =
# 1 1 1
print("XOR: %s (%i)" % (bin(bit_xor), bit_xor))

# << сдвиг влево, равносилен умножению на 2^n
print("Left shift: %s (%i)" % (bin(left_shift), left_shift))

# >> сдвиг вправо, равносилен делению на 2^n
print("Left shift: %s (%i)" % (bin(right_shift), right_shift))
