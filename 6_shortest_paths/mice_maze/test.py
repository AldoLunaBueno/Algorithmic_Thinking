import pytest
import subprocess
import sys

# PATHS ARE ALL YOU NEED TO CHANGE:
PATH_TO_SCRIPT = "mice_maze.py"
PATH_TO_TEST_CASES_1 = "test_cases.txt"
PATH_TO_TEST_CASES_2 = "test_heavy.txt"

def load_test_cases(file_name):
    # Read the file and separate the test cases by '==='
    with open(file_name, "r") as f:
        content = f.read().strip()
    
    cases = content.split('===')
    test_cases = []
    
    for case in cases:
        # Split each case into input and output using '---'
        input_data, expected = case.strip().split('---')
        test_cases.append((input_data.strip(), expected.strip()))
    
    return test_cases

@pytest.mark.parametrize("input_data, expected", load_test_cases(PATH_TO_TEST_CASES_1))
def test_multiple_cases(input_data, expected):
    _test_from_data(input_data, expected)

@pytest.mark.parametrize("input_data, expected", load_test_cases(PATH_TO_TEST_CASES_2))
def test_heavy_cases(input_data, expected):
    _test_from_data(input_data, expected)


def _test_from_data(input_data, expected):
    # Run the script as a subprocess, pass input and get result
    result = subprocess.run(
        [sys.executable, # get the current Python interpreter
         PATH_TO_SCRIPT],
        input=input_data,
        text=True,
        capture_output=True
    )
    out = result.stdout.strip()
    
    # Compare the output with the expected result
    assert out == expected