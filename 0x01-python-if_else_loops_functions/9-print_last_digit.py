#!/usr/bin/python3
def print_last_digit(number):
    determer = 1
    if number < 0:
        number *= -1
        determer = -1
    return (number % 10) * determer
