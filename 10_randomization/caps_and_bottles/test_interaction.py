import pytest
from communication_inter import Communication
from time import time

path_to_script = "caps_and_bottles.py"
path_to_test_cases = "interactive_test_cases.txt"
timeout = 5

def _test_interaction(input_data: str, expected: str, interactive_data: str):
    output_lines = []
    caps, bottles = interactive_data.split("\n")
    caps = [None] + [int(x) for x in caps.strip().split(" ")]
    bottles = [None] + [int(x) for x in bottles.strip().split(" ")]

    start_time = time()
    with Communication(path_to_script) as c:
        c.write(input_data.strip())
        while not c.isfinish() and time() - start_time < timeout:
            line = c.read()
            if line is None:
                continue
            if line[0] == "1": # script answering partial result
                output_lines.append(line)
            elif line[0] == "0": # script asking
                _, i, j = [int(x) for x in line]
                if caps[i] < bottles[j]:
                    c.write("-1")
                elif caps[i] > bottles[j]:
                    c.write("1")
                elif caps[i] == bottles[j]:
                    c.write("0")
    
    output_lines = sorted(output_lines)
    output = "\n".join(output_lines)

    # Compare the output with the expected result
    assert output == expected
    
def load_interactive_test_cases(file_name):
    # Read the file and separate the test cases by '==='
    with open(file_name, "r") as f:
        content = f.read().strip()
    
    cases = content.split('===')
    test_cases = []
    
    for case in cases:
        # Split each case into input and output using '---'
        input_data, expected, interactive_data = case.strip().split('---')
        test_cases.append((input_data.strip(), expected.strip(), interactive_data.strip()))
    
    return test_cases

# Load test cases from file
test_cases = load_interactive_test_cases(path_to_test_cases)

@pytest.mark.parametrize("input_data, expected, interactive_data", test_cases)
def test_multiple_cases(input_data, expected, interactive_data):
    _test_interaction(input_data, expected, interactive_data)