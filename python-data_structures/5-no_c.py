#!/usr/bin/python3
def no_c(my_string):
    list_cast = list(my_string)
    new_list = []
    for i in list_cast:
        if i != 'c' and i != 'C':
            new_list.append(i)
    #sep = ""
    return "".join(new_list)
