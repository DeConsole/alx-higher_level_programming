#!/usr/bin/python3
for a in range(20, 46):
    if a == 36 or a == 24:
        continue
    print("{:c}".format(a), end=" ")
