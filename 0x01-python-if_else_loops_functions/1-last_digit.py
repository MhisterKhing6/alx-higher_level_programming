#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Ldigit = number % 10
lmessge = f"Last digit of {number}  is {Ldigit}"
if Ldigit > 0:
    print(f"{lmessge} and is greater than 5")
if Ldigit == 0:
    print(f"{lmessge} and is zero")
if Ldigit < 6:
    print(f"{lmessge}  less than6 and not 0")
