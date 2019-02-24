import random

print("I made a number in range from 0 to 100, guess it")

random_number = random.randint(0, 100)

for i in range(0, 10):
    num = int(input("Enter number: "))
    if num == random_number:
        print("You are right!")
        break

    if i == 9:
        print(f"You are lost :( The number was: {random_number}.")
    else:
        print(f"Nope, number should be {'greater' if num < random_number else 'less'}")
