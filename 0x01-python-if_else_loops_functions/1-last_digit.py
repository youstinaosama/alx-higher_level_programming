#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ldig = number % -10
elif number >= 0:
    ldig = number % 10
if ldig == 0:
    print(f"Last digit of {number} is {ldig} and is 0")
elif ldig > 5:
    print(f"Last digit of {number} is {ldig} and is greater than 5")
else:
    print(f"Last digit of {number} is {ldig} and is less than 6 and not 0")
