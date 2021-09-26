#!/usr/bin/env python3

"""Functions for transposing matrices."""

import os


def transpose_matrix(file_name='matrix.txt', file_name_new='trans_matrix.txt', file_path=os.getcwd()):
    """Get matrix from file and transpose it.

    Arguments:
        file_name (str) - the name of the file in which
            the matrix is located (default: 'matrix.txt')
        file_name_new (str) - the name of the file in which
            the matrix will be saved (default: 'trans_matrix.txt')
        file_path (str) - the path where the file with
            the matrix is located (default: script launch location)
    """
    full_path = os.path.join(file_path, file_name)
    full_path_new = os.path.join(file_path, file_name_new)
    with open(full_path, 'r') as file:
        rows = len(file.readline()) - 1
        file.seek(0)
        with open(full_path_new, 'w') as file_new:
            for number_row in range(rows):
                for row in file:
                    file_new.write(row[number_row])
                if number_row != rows - 1:
                    file_new.write('\n')
                file.seek(0)
    print(f'Transposed matrix successfully saved to {full_path_new}')


def main():
    """Running the matrix_transposer."""
    transpose_matrix()


if __name__ == '__main__':
    main()
