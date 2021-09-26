#!/usr/bin/env python3

"""Functions for creating matrices."""

import os
from random import randint

# Constants for setting matrix size.
ROWS = 5
COLUMNS = 5


def generate_matrix(rows, columns, init_val=0, end_val=9, file_name='matrix.txt', file_path=os.getcwd()):
    """Generate matrix and save to the file.

    Arguments:
        rows (int) - number of rows in the matrix
        columns (int) - number of columns in the matrix
        init_val (int) - the initial value of the range of
            values of the matrix (default: 0)
        end_value (int) - the end value of the range of
            values of the matrix (default: 9)
        file_name (str) - the name of the file in which
            the matrix will be saved (default: 'matrix.txt')
        file_path (str) - the path where the matrix file will
            be saved (default: script launch location)
    """
    full_path = os.path.join(file_path, file_name)
    with open(full_path, 'w') as file:
        for row in range(rows):
            row_items = [str(randint(init_val, end_val)) for _ in range(columns)]
            row_items_str = ''.join(row_items)
            if row != rows - 1:
                row_items_str += '\n'
            file.write(row_items_str)
    print(f'Matrix has successfully saved to {full_path}')


def main():
    """Running the matrix_generator."""
    generate_matrix(ROWS, COLUMNS)


if __name__ == '__main__':
    main()
