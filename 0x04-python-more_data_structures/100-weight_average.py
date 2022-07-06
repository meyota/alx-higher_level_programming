#!/usr/bin/python3
def weight_average(my_list=[]):
    return sum(x * y for x, y in zip(x, y)) / sum(y)
