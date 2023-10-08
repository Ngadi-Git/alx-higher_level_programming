#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for index in range(len(matrix)):
        for jdx in range(len(matrix[index])):
                print("{:d}".format(matrix[index][jdx]), end="")
                if jdx != (len(matrix[index]) - 1):
                    print(" ", end="")

        print()
