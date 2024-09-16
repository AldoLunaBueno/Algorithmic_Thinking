import pytest
import sys
import io
from river_hopscotch import main

parametrize = pytest.mark.parametrize

def _test(capsys: pytest.CaptureFixture[str], input, expected):
    input = "\n".join(input) + "\n"
    sys.stdin = io.StringIO(input)
    main()
    out, err = capsys.readouterr()
    assert out == expected + "\n"

@parametrize("input, expected", [
    (("12 2 1", "5", "8"), "5"),
    (("12 4 2", "1", "3", "8", "9"), "3"),
    (("25 5 2", "2", "14", "11", "21", "17"), "4"),
    (("12 4 2", "2", "4", "5", "8"), "4")
])
def test_complex(capsys: pytest.CaptureFixture[str], input, expected):
    _test(capsys, input, expected)