"""Tests for matrix loader"""

import os
import pytest
import tempfile
from matrix_handler.matrix_generator import generate_matrix
from matrix_handler.matrix_transposer import transpose_matrix


@pytest.mark.parametrize('rows, columns', [(5, 5), (10, 5)])
def test_generate_matrix(rows, columns):
    with tempfile.TemporaryDirectory() as tmpdirname:
        generate_matrix(rows, columns, file_name='matrix.txt', file_path=tmpdirname)
        path = os.path.join(tmpdirname, 'matrix.txt')
        assert os.path.exists(path)
        with open(path, 'r') as file:
            real_rows = len(file.readline()) - 1
            file.seek(0)
            real_columns = 0
            for _ in file:
                real_columns += 1
            file.seek(0)
            if rows == columns:
                assert rows == real_rows
                assert columns == real_columns
            else:
                assert rows == real_columns
                assert columns == real_rows
            for item in file.read():
                if item != '\n':
                    assert int(item) >= 0 and int(item) <= 9


@pytest.mark.parametrize(
    'matrix, trans_matrix',
    [
        ('123\n456\n789', '147\n258\n369'),
        ('12\n34\n56\n78', '1357\n2468')
    ]
)
def test_transpose_matrix(matrix, trans_matrix):
    with tempfile.TemporaryDirectory() as tmpdirname:
        path = os.path.join(tmpdirname, 'matrix.txt')
        with open(path, 'w') as file:
            file.write(matrix)
        transpose_matrix(file_name='matrix.txt', file_name_new='trans_matrix.txt', file_path=tmpdirname)
        path_new = os.path.join(tmpdirname, 'trans_matrix.txt')
        assert os.path.exists(path_new)
        with open(path_new, 'r') as file:
            assert trans_matrix == file.read()
