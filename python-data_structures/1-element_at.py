#!/usr/bin/python3
def element_at(my_list, idx):
    idx_max = len(my_list) - 1
    if idx < 0 or idx > idx_max:
        return None
    else:
        return my_list[idx]
