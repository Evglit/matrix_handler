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
    rows = param_processing('Number of rows:', 'Rows must be number!')
    columns = param_processing('Number of columns:', 'Columns must be number!')
    return rows, columns


def param_processing(massage, massage_error):
    while True:
        answer = input(f'{massage} ')
        try:
            answer = int(answer)
            break
        except ValueError:
            print(massage_error)
            answer = None
    return answer
