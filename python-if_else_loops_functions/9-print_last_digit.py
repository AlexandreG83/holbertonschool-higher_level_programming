#!/usr/bin/python3
def print_last_digit(i):
    last_digit = abs(i) % 10
    print("{}".format(last_digit), end="")
    return last_digit

