#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in my_list:
        count += 1
    try:
        if x > count:
            raise ValueError
        j = 0
        while j != x:
            print("{:d}".format(my_list[j]), end="")
            j += 1
        print()
        return x
    except ValueError:
        j = 0
        while j != count:
            print("{:d}".format(my_list[j]), end="")
            j += 1
        print()
        return count
