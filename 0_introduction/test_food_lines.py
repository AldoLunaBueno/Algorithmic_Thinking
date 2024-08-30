import pytest
import sys
import io
import food_lines

parametrize = pytest.mark.parametrize

@parametrize("N_M, n_lines, expected",
                [
                    ("1 1", "0", "0\n"),
                    ("1 1", "1", "1\n"),
                    ("1 2", "0", "0\n1\n"),
                    ("1 2", "1", "1\n2\n"),
                    ("1 3", "0", "0\n1\n2\n"),
                ])
def test_one_line(capsys, N_M, n_lines, expected):
    sys.stdin = io.StringIO(f"{N_M}\n{n_lines}")
    food_lines.solve() # print solution
    out, err = capsys.readouterr()
    assert out == expected

@parametrize("N_M, n_lines, expected",
                [
                    ("2 1", "0 0", "0\n"),
                    ("2 1", "1 0", "0\n"),
                    ("2 1", "1 1", "1\n"),
                    ("2 2", "0 0", "0\n0\n"),
                    ("2 2", "1 0", "0\n1\n"),
                    ("2 2", "1 1", "1\n1\n"),
                    ("2 3", "0 0", "0\n0\n1\n"),
                ])
def test_two_lines(capsys, N_M, n_lines, expected):
    sys.stdin = io.StringIO(f"{N_M}\n{n_lines}")
    food_lines.solve() # print solution
    out, err = capsys.readouterr()
    assert out == expected

@parametrize("N_M, n_lines, expected",
                [
                    ("5 3", "2 2 3 3 3", "2\n2\n3\n")
                ])
def test_n_lines(capsys, N_M, n_lines, expected):
    sys.stdin = io.StringIO(f"{N_M}\n{n_lines}")
    food_lines.solve() # print solution
    out, err = capsys.readouterr()
    assert out == expected