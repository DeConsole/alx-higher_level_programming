#!/usr/bin/python3
for number1 in range(0, 10):
    for number2 in range(0, 10):
        if number1 is 8 and number2 is 9:
            print("{:d}{:d}".format(number1, number2))
        elif number1 < number2:
            print("{:d}{:d}".format(number1, number2), end=", ")
