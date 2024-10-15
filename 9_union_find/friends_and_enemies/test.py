import os
import subprocess
import sys
import pytest

# PATHS ARE ALL YOU NEED TO CHANGE:
PATH_TO_SCRIPT = "friends_and_enemies.py"
PATH_TO_TEST_CASES = "test_cases.txt"

def load_test_cases(file_name):
    with open(file_name, "r") as f:
        content = f.read().strip()
    
    cases = content.split('===')
    test_cases = []
    
    for case in cases:
        input_data, expected = case.strip().split('---')
        test_cases.append((input_data.strip(), expected.strip()))
    
    return test_cases

# Load test cases from file
test_cases = load_test_cases(PATH_TO_TEST_CASES)

@pytest.mark.parametrize("input_data, expected", test_cases)
def test_multiple_cases(input_data, expected):
    _test_from_data(input_data, expected)

def _test_from_data(input_data, expected):
    # Ensure the coverage environment variable is set for the subprocess
    env = os.environ.copy()
    env["COVERAGE_PROCESS_START"] = os.path.abspath(".coveragerc")
    
    # Run the script as a subprocess, pass input and get result
    result = subprocess.run(
        [sys.executable, PATH_TO_SCRIPT],
        input=input_data,
        text=True,
        capture_output=True,
        env=env
    )
    
    out = result.stdout.strip()
    
    # Compare the output with the expected result
    assert out == expected
