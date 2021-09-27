"""Command line interface for matrix handler."""


def get_param():
    """Get parameters of matrix from the user and check them.

    Retrur
    ------
    rows : int
        number of rows
    columns : int
        number of columns

    """
    print('Enter the parameters of the matrix.')
    while True:
        rows = input('Number of rows: ')
        try:
            rows = int(rows)
            break
        except ValueError:
            print('Rows must be number!')
            rows = None

    while True:
        columns = input('Number of columns: ')
        try:
            columns = int(columns)
            break
        except ValueError:
            print('Columns must be number!')
            columns = None

    return rows, columns
