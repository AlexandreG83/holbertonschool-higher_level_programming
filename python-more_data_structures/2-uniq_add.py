#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    stock = set()

    for i in my_list:
        if i not in stock:
            result += i
            stock.add(i)

    return result
