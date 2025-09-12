#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = len(matrix[0])
    b = len(matrix)
    new_mat = [[0 for x in range(a)] for x in range(b)]
    for i in range(b):
        for j in range(a):
            new_mat[i][j] = matrix[i][j] ** 2
    return new_mat
