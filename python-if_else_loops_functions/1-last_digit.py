#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = 0

if number < 0:
    temp = -number
    temp %= 10
    temp *= -1
else:
    temp = number
    temp %= 10

if temp > 5:
    print(f"Last digit of {number} is {temp} and is greater than 5")
elif temp == 0:
    print(f"Last digit of {number} is {temp} and is 0")
else:
    print(f"Last digit of {number} is {temp} and is less than 6 and not 0")
