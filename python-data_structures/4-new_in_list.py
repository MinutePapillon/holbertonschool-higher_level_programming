#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    j = 0
    for i in my_list:
        new_list.append(i)
    new_list[idx] = element
    return new_list
