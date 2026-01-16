#!/usr/bin/python3
for i, c in enumerate(range(122, 96, -1)):
    letter = chr(c)
    if i % 2:
        letter = letter.upper()
    print(letter, end='')
