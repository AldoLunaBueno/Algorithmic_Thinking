import pytest
import sys
import io
import feeding_ants

parametrize = pytest.mark.parametrize
ALLOWED_ABSOLUTE_ERR = 0.001

@parametrize("input, expected", [
    (("6", "1 2 20 0", "1 3 50 0", "1 4 30 1", "4 5 50 0", "4 6 50 0", "-1 2 9 -1 7 8"), "18.0"),
    (("5", "1 2 50 0", "1 3 50 0", "2 4 25 0", "2 5 75 1", "-1 -1 4 1 9"), "8.00"),
    (("3", "1 2 20 1", "1 3 80 1", "-1 4 8"), "10.0000"),
    (("6", "1 2 100 1", "2 3 20 0", "2 4 20 0", "2 5 60 0", "4 6 100 1", "-1 -1 1 -1 1 2"), "2.659")
])
def test_samples(capsys: pytest.CaptureFixture[str], input, expected):
    _test(capsys, input, expected)

def _test(capsys: pytest.CaptureFixture[str], input, expected):
    input = "\n".join(input) + "\n"
    sys.stdin = io.StringIO(input)
    feeding_ants.main()
    out, err = capsys.readouterr()
    out, expected = float(out), float(expected)
    assert abs(out - expected) <= ALLOWED_ABSOLUTE_ERR