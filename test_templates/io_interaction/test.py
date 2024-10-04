import pytest
from communication_inter import Communication
from time import time


PATH_TO_SCRIPT = "script_to_test.py"
PATH_TO_TEST_CASES = "test_cases.txt"
TIMEOUT = 5

# THIS IS WHERE YOU NEED TO CODE
def _test_interaction(input_data: str, expected: str, interactive_data: str):
    # Example of specific interaction
    MESSAGE_SIZE = 5
    output_lines = []
    caps, bottles = interactive_data.split("\n")
    caps = [None] + [int(x) for x in caps.strip().split(" ")]
    bottles = [None] + [int(x) for x in bottles.strip().split(" ")]

    start_time = time()
    with Communication(PATH_TO_SCRIPT) as c:
        c.write(input_data.strip())
        while not c.isfinish() and time() - start_time < TIMEOUT:
            line = c.read()
            # validation
            if line is None or len(line) != MESSAGE_SIZE:
                break
            line = line.strip()
            print(repr(line))
            if line[0] == "1": # script answering partial result
                output_lines.append(line)
            elif line[0] == "0": # script asking
                _, i, j = [int(x) for x in line.split(" ")]
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

# THIS IS ALWAYS THE SAME FOR THIS KIND OF TEST:

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
test_cases = load_interactive_test_cases(PATH_TO_TEST_CASES)

@pytest.mark.parametrize("input_data, expected, interactive_data", test_cases)
def test_multiple_cases(input_data, expected, interactive_data):
    _test_interaction(input_data, expected, interactive_data)