#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    number_max = my_list[0]
    for i in my_list:
        if number_max < i:
            number_max = i
    return number_max
