# Problem: Snowflakes
# Judge: DMOJ 
# ID: cco07p2

from typing import List

ARMS = 6
TWIN_MSG = "Twin snowflakes found."
NO_TWIN_MSG = "No two snowflakes are alike."

def main():
    n, n_lines = get_data()
    solve(n, n_lines)

def get_data():
    n = int(input())
    n_lines = []
    for _ in range(n):
        line = input()
        line = line.split(" ")
        line = [int(x) for x in line]
        n_lines.append(line)
    return n, n_lines

def solve(n, n_lines):
    for i in range(n):
        for j in range(i+1, n):
            if identical(n_lines[i], n_lines[j]):
                print(TWIN_MSG)
                return
    print(NO_TWIN_MSG)

def identical(line_1: List, line_2: List) -> bool:
    """
    Returns True if lists are identical with some rotation clockwise (rigth) of counterclockwise (left)
    """
    for start in range(ARMS): # start for line_2
        if (identical_right(line_1, line_2, start) 
            or identical_left(line_1, line_2, start)):
            return True
    return False

def identical_right(line_1, line_2, start):
    for offset in range(ARMS): # one by one arm
        if line_1[offset] != line_2[(start+offset) % ARMS]:
            return False # early verification
    return True

def identical_left(line_1, line_2, start):
    for offset in range(ARMS): # one by one arm
        if line_1[offset] != line_2[start-offset]:
            return False # early verification
    return True


if __name__ == "__main__":
    main()