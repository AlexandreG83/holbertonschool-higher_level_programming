#!/usr/bin/python3
for i in range(26):
    letter = chr(122 - i)
    if i % 2:
        letter = letter.upper()
    print(letter, end='')
