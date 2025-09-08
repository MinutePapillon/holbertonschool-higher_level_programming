#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for l, j in enumerate(i):
            print("{}".format(j), end=" " if l != len(i) - 1 else "")
        print()
