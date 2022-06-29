#!/usr/bin/python3
def uppercase(str):
    for n in str:
        n = ord(n)
        if 97 <= n <= 122:
            n = n - 32
        print("{:c}".format(n), end='')
    print()
