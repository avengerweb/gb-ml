import os

MODIFIER = 31

for i in range(32, 128):
    print(f"{i} - {chr(i)}", end=os.linesep if (i - MODIFIER) % 10 == 0 else " ")
