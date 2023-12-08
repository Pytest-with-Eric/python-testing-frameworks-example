# Python Testing Frameworks
This repo contains the sample code for the article - [Practical Overview Of The Top 5 Python Testing Frameworks](https://pytest-with-eric.com/comparisons/python-testing-frameworks/)

# Requirements
* Python (3.11+)
* Please see `requirements.txt` for the list of dependencies

# Repo Overview
```shell
├── .gitignore
├── README.md
├── requirements.txt
├───src
│   └── check_number.py
└───tests
    ├── number_tests.robot
    ├── test_check_number_with_nose2.py
    ├── test_check_number_with_pytest.py
    └── test_check_number_with_unittest.py
```

Please install the dependencies via the `requirements.txt` file using 
```bash
pip install -r requirements.txt
```
If you don't have Pip installed, please follow instructions online on how to do it.

# How To Run the Unit Tests
To run the Unit Tests from the root of the repo, run

## Pytest
```bash
pytest -v
```

## Unittest
```bash
python -m unittest
```

## Nose2
```bash
nose2 -v
```

## DocTest
```bash
python src/check_number.py -v
```

## Robot Framework
```bash
robot tests/number_tests.robot
```

If you have any questions about the project, please raise an Issue on GitHub. 
