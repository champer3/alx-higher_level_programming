#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num1 = number % 10
if num1 > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, number[-1]))
elif num1 == 0:
    print("Last digit of {:d} is {:d} and is zero".format(number, number[-1]))
elif num1 < 6 && num1 != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, number[-1]))
