#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
determer = 1
Ldigit = 1
if number < 0:
    number *= -1
    determer = -1
Ldigit = number % 10
Lmessage = f" Last digit of {number*determer} is {Ldigit*determer} "

if Ldigit > 5:
    print(f"{Lmessage } and is greater than 5")
elif Ldigit == 0:
    print(f"{Lmessage} and is 0")
else:
    print(f"{Lmessage} and is less than 6 and not 0")
