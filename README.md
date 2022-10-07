# Task 28.1 Intro

I used the Page Object Template with Selenium and Python (PyTest + Selenium) by Timur Nurlygayanov. Link: https://github.com/TimurNurlygayanov/ui-tests-example

In the task, the site of the Labyrinth online store was selected.
In the process of work, 65 tests were formed.

## About files in
:white_check_mark: **`conftest.py`** contains all the necessary code to catch failed test cases and take a screenshot of the page in case any test case fails.

:white_check_mark: **`pages/base.py`** contains the implementation of the page object template for Python.

:white_check_mark: **`pages/elements.py`** contains a helper class for defining web elements on web pages.

:white_check_mark: **`pages/......py`** contain classes and locators for the objects under test

:white_check_mark: **`tests/test_labirint_authorization.py`** contains authorization tests

:white_check_mark: **`tests/test_test_labirint_cart.py`** contains Cart tests

:white_check_mark: **`tests/test_labirint_postponed.py`** contains Postponed tests

:white_check_mark: **`tests/test_labirint_search.py`** contains search tests
