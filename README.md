# Matrix handler
[![Python CI](https://github.com/Evglit/matrix_handler/actions/workflows/pyci.yml/badge.svg)](https://github.com/Evglit/matrix_handler/actions/workflows/pyci.yml)
<a href="https://codeclimate.com/github/Evglit/matrix_handler/maintainability"><img src="https://api.codeclimate.com/v1/badges/3d287c36a89eaa0415b6/maintainability" /></a>
<a href="https://codeclimate.com/github/Evglit/matrix_handler/test_coverage"><img src="https://api.codeclimate.com/v1/badges/3d287c36a89eaa0415b6/test_coverage" /></a><br>

## Description
This package generates a matrix of the specified size and saves it to the "matrix.txt" file. Then it transposes the matrix and saves it to the "trans_matrix.txt" file. Matrix files are created in the directory where the program is launched.<br>
`Note: Creation and transposition of large matrices 10000x10000 and more, can take a long time.`

## Installation
Clone the repository, open the package in the command line and run these commands:<br>
``` bash
make build
make package-install
```
Or just run the command:
``` bash
pip install --user --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ matrix-handler
```

## Usege
After successful installation, run in the command line:
``` bash
matrix-handler
```