#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    del my_list[idx]
    for i in my_list:
        new_list.append(i)
    return new_list
