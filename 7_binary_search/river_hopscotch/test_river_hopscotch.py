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
    (("25 5 2", "14", "11", "21", "17"), "4")
])
def test_complex(capsys: pytest.CaptureFixture[str], input, expected):
    _test(capsys, input, expected)