import pytest
import sys
import io

import snowflakes

parametrize = pytest.mark.parametrize

# Two possible expected printed values
# for snowflakes.main()
TWIN_MSG = "Twin snowflakes found."
NO_TWIN_MSG = "No two snowflakes are alike."

@parametrize("n, n_snowflakes", [
    ("1", ("0 0 0 0 0 0", ))
])
def test_no_arm_assert_no_twin(capsys: pytest.CaptureFixture[str], 
                          n, n_snowflakes):
    expected = NO_TWIN_MSG
    __test(capsys, n, n_snowflakes, expected)

@parametrize("n, n_snowflakes", [
    ("2", ("0 0 0 0 0 0", 
           "1 0 0 0 0 0")
    ),
    ("3", ("1 0 0 0 0 0", 
           "2 0 0 0 0 0",
           "3 0 0 0 0 0")
    )
])
def test_one_arm_assert_no_twin(capsys: pytest.CaptureFixture[str], 
                      n, n_snowflakes):
    expected = NO_TWIN_MSG
    __test(capsys, n, n_snowflakes, expected)

@parametrize("n, n_snowflakes", [
    ("2", ("1 0 0 0 0 0", 
           "1 0 0 0 0 0")
    ),
    ("3", ("1 0 0 0 0 0",
           "0 0 0 0 0 0",
           "1 0 0 0 0 0")
    ),
    ("4", ("0 1 0 0 0 0",
           "0 0 2 0 0 0",
           "0 0 0 3 0 0",
           "0 1 0 0 0 0")
    )           
])
def test_one_arm_assert_twin(capsys: pytest.CaptureFixture[str], 
                      n, n_snowflakes):
    expected = TWIN_MSG
    __test(capsys, n, n_snowflakes, expected)

@parametrize("n, n_snowflakes", [
    ("2", ("1 0 0 0 0 0", 
           "1 1 0 0 0 0")
    ),
    ("3", ("1 0 0 0 0 1",
           "0 0 1 0 0 1",
           "1 0 1 0 0 0")
    )      
])
def test_rotation_assert_no_twin(capsys: pytest.CaptureFixture[str], 
                      n, n_snowflakes):
    expected = NO_TWIN_MSG
    __test(capsys, n, n_snowflakes, expected)

@parametrize("n, n_snowflakes", [
    ("2", ("1 0 0 0 0 0", 
           "0 1 0 0 0 0")
    ),
    ("3", ("1 1 0 0 0 0",
           "0 0 1 0 0 1",
           "0 0 0 1 1 0")
    ),
    ("4", ("1 0 0 0 1 0",
           "1 0 0 0 0 1",
           "1 0 0 1 0 0",
           "0 1 0 1 0 0")
    ),
])
def test_rotation_assert_twin(capsys: pytest.CaptureFixture[str], 
                      n, n_snowflakes):
    expected = TWIN_MSG
    __test(capsys, n, n_snowflakes, expected)

@parametrize("n, n_snowflakes", [
    ("2", ("1 2 3 4 5 6", 
           "6 5 4 3 2 1")
    ),
    ("2", ("1 2 3 4 5 6",
           "4 3 2 1 6 5")
    ),
])
def test_reflexion_assert_twin(capsys: pytest.CaptureFixture[str], 
                      n, n_snowflakes):
    expected = TWIN_MSG
    __test(capsys, n, n_snowflakes, expected)

def __test(capsys, n, n_snowflakes, expected):
    all_lines = []
    all_lines.append(n)
    for line in n_snowflakes:
        all_lines.append(line)
    all_lines = "\n".join(all_lines)
    sys.stdin = io.StringIO(all_lines)

    snowflakes.main()
    out, err = capsys.readouterr()
    assert out == expected