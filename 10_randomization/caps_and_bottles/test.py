import pytest
from subprocess import run, Popen, PIPE
import sys

path_to_script = "caps_and_bottles.py"
path_to_test_cases = "test_cases.txt"

def interactive_process():
    with Popen([sys.executable, path_to_script], stdout=PIPE) as p:
        while True:
            # https://docs.python.org/3/library/io.html#io.BufferedIOBase.read1
            text = p.stdout.read1().decode("utf-8")ç
            p.comuni
            print(text, end='', flush=True)

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
test_cases = load_test_cases(path_to_test_cases)

@pytest.mark.parametrize("input_data, expected", test_cases)
def test_multiple_cases(input_data, expected):
    _test_from_data(input_data, expected)

def _test_from_data(input_data, expected):
    # Run the script as a subprocess, pass input and get result
    result = run(
        [sys.executable, # get the current Python interpreter
         path_to_script],
        input=input_data,
        text=True,
        capture_output=True
    )
    out = result.stdout.strip()
    
    # Compare the output with the expected result
    assert out == expected