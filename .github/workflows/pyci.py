name: Python CI

on:
  - push
  - pull_request

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        # we want to test our package on several versions of Python
        python-version: [3.6, 3.7, 3.8]
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}
        # make depends on poetry
      - name: Install dependencies
        run: |
          pip install poetry
          make install
      - name: Run linter and pytest
        run: |
          make check
      - name: Test & publish code coverage
        uses: paambaati/codeclimate-action@v2.7.4
        env:
          CC_TEST_REPORTER_ID: ${{ secrets.CC_TEST_REPORTER_ID }}
        with:
          debug: true