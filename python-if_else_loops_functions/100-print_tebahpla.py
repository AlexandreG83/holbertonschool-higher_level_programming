#!/usr/bin/python3
for i in range(25, -1, -1):
    case = ord('a') + i
    if i % 2:
        case = chr(case)
    else:
        case = chr(case).upper()
    print("{}".format(case), end='')
