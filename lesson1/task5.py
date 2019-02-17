# Diagram: https://drive.google.com/file/d/1e-JDR2DLXA0dEzCv48TnJyutxd25F8rf/view?usp=sharing
# No validation required (good user)
letter1 = str(input("Input first letter: "))
letter2 = str(input("Input second letter: "))

# Philologists is not a programmers, the first letter in alphabet has position - 1
first_letter_pos = ord('a') - 1

letter1_pos = ord(letter1) - first_letter_pos
letter2_pos = ord(letter2) - first_letter_pos

# We got position difference including last letter, so we should subtract 1
diff = abs(letter1_pos - letter2_pos) - 1

print("Position of %s: %i" % (letter1, letter1_pos))
print("Position of %s: %i" % (letter2, letter2_pos))
print("Letters between: %i" % diff)
