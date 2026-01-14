#!/usr/bin/python3
"""Print numbers from 00 to 99 separated by a comma"""
for i in range(100):
    if i != 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))
