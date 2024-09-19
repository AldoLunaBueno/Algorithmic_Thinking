import pytest
import sys
import io

from homer_simpson import main

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

# Load test cases from file
test_cases = load_test_cases("test_cases.txt")

@pytest.mark.parametrize("input_data, expected", test_cases)
def test_multiple_cases(capsys: pytest.CaptureFixture[str], input_data, expected):
    _test_from_data(capsys, input_data, expected)

def _test_from_data(capsys: pytest.CaptureFixture[str], input_data, expected):
    # Sets standard input (sys.stdin)
    sys.stdin = io.StringIO(input_data)
    
    main() # method to be tested

    # Capture the output
    out, err = capsys.readouterr()
    
    # Compare the output with the expected result
    assert out.strip() == expected