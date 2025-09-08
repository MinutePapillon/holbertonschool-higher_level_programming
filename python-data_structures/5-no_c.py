#!/usr/bin/python3
def no_c(my_string):
    new_list = []
    for i in list(my_string):
        if i != 'c' and i != 'C':
            new_list.append(i)
    return "".join(new_list)
