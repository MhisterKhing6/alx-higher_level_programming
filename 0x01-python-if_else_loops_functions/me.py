#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
determer = -1
mod = 1
Ldigit = 1;
print (number)

if number < 0:
    number *= -1
    determerer = -1;

if number <100:
    Ldigit = number % 10
elif number < 1000:
    Ldigit = number % 100
else:
    Ldigit = number % 10000

print(f"f{number * determerer}  {Ldigit}")


