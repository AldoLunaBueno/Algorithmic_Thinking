import pytest
import sys
import io

import promotion

parametrize = pytest.mark.parametrize


def _test(capsys: pytest.CaptureFixture[str], input, expected):
    input = "\n".join(input) + "\n"
    sys.stdin = io.StringIO(input)
    promotion.main()
    out, err = capsys.readouterr()
    assert out == expected

@parametrize("input, expected",
             [
                 (("2", "16 6 63 16 82 25 2 43 5 17 10 56 85 38 15 32 91", "1 57"), "169\n"), 
                 (("5", "3 1 2 3", "2 1 1", "4 10 5 5 1", "0", "1 2"), "19\n")
                 
             ])
def test_complex(capsys: pytest.CaptureFixture[str], input, expected):
    _test(capsys, input, expected)