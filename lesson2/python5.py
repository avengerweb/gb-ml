import os

mod = 31

for i in range(32, 128):
    print(f"{i} - {chr(i)}", end=os.linesep if (i - mod) % 10 == 0 else " ")
