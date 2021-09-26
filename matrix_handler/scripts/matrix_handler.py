#!/usr/bin/env python3

"""Matrix handler script."""

from matrix_handler.matrix_generator import generate_matrix
from matrix_handler.matrix_transposer import transpose_matrix


def main():
    generate_matrix(10, 10)
    transpose_matrix()


if __name__ == '__main__':
    main()
