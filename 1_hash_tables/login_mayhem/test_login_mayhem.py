import pytest
import sys
import io

import login_mayhem

parametrize = pytest.mark.parametrize

def _test(capsys: pytest.CaptureFixture[str],
          q, queries, expected):
    queries = "\n".join(queries)
    lines = q + "\n" + queries  + "\n"
    sys.stdin = io.StringIO(lines)
    login_mayhem.main()
    out, err = capsys.readouterr()
    assert out == expected

@parametrize("q, queries, expected", [
    ("1", ("1 a",), ""),
    ("1", ("2 a",), "0\n"),
    ("2", ("1 a", 
           "2 b"), "0\n"),
    ("2", ("1 a", 
           "2 a"), "1\n"),
])
def test_trivial(capsys: pytest.CaptureFixture[str], 
                 q, queries, expected):
    _test(capsys, q, queries, expected)


@parametrize("q, queries, expected", [
    ("5", ("1 aaa", 
           "2 aa", 
           "1 aa", 
           "2 aa", 
           "1 abb"), "1\n2\n"),
         
    ("4", ("1 x", 
           "1 x", 
           "1 xy", 
           "2 x"), "3\n"),

    ("7", ("1 mir", 
           "1 mirta", 
           "1 ta", 
           "1 ir", 
           "1 t", 
           "2 t", 
           "2 mir"), "3\n2\n")
])
def test_complex(capsys: pytest.CaptureFixture[str], 
                 q, queries, expected):
    _test(capsys, q, queries, expected)