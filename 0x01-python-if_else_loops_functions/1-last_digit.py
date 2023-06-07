#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

stringNumber = repr(number)
lastN = int(stringNumber[-1])

if lastN > 5:
    print(f"Last digit of {number} is {lastN} and is greated than 5")
elif lastN == 0:
    print(f"Last digit of {number} is {lastN} and is 0")
else:
    print(f"Last digit of {number} is {lastN} and is less than 6 and not 0")
