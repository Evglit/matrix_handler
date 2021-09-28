# Matrix handler
[![Python CI](https://github.com/Evglit/matrix_handler/actions/workflows/pyci.yml/badge.svg)](https://github.com/Evglit/matrix_handler/actions/workflows/pyci.yml)
<a href="https://codeclimate.com/github/Evglit/matrix_handler/maintainability"><img src="https://api.codeclimate.com/v1/badges/3d287c36a89eaa0415b6/maintainability" /></a>
<a href="https://codeclimate.com/github/Evglit/matrix_handler/test_coverage"><img src="https://api.codeclimate.com/v1/badges/3d287c36a89eaa0415b6/test_coverage" /></a><br>

## Description
Generates a matrix of the specified size and saves it to the "matrix.txt" file. Then transapans the matrix and saves it to the "trans_matrix.txt" file. Matrix files are created where the program is launched.<br>
``` bash
Note: Creation and transposition of large matrices 10000x10000 and more, can take a long time.
```

## Installation
Clone the repository, open the package in the command line and run these commands:<br>
``` bash
make build
make package-install
```

## Usege
After successful installation, run in the command line:
``` bash
matrix-handler
```