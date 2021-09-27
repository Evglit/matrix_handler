#!/usr/bin/env python3

"""Matrix handler script."""

from matrix_handler.cli import get_param
from matrix_handler.matrix_generator import generate_matrix
from matrix_handler.matrix_transposer import transpose_matrix


def main():
    rows, columns = get_param()
    generate_matrix(rows, columns)
    transpose_matrix()


if __name__ == '__main__':
    main()
