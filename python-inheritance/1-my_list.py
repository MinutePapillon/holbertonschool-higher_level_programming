#!/usr/bin/python3
"""
1-my_list.py
Module that defines a class MyList inheriting from list.
"""


class MyList(list):
    """
    A subclass of list with a public method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        Does not modify the original list.
        """
        print(sorted(self))