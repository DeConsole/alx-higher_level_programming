#!/usr/bin/python3
def fizzbuzz():
    for digit in range(1, 101):
        if digit % 3 is 0:
            print("Fizz", end=" ")
        elif digit % 5 is 0:
            print("Buzz", end=" ")
        elif digit % 15 is 0:
            print("FizzBuzz", end=" ")
        else:
            print(digit, end=" ")
