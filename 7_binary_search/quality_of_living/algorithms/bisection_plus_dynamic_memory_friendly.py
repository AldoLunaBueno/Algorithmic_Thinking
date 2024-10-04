from typing import List, Callable
Matrix = List[List[int]]

# Resources: 6.761s, 289.61 MB
# Final score: 80/100 (12.0/15 points)
# MLE (Memory Limit Exceeded)

# main() function was optimized with sys.stdin.readline() 
# instead of input() built-in function

def solve(r: int, c: int, h: int, w: int, q: Matrix):
    min_quality = h*w//2
    max_quality = r*c + 1 - h*w//2
    f = lambda x: not can_make_quality(x, r, c, h, w, q)
    result = discrete_bisection_method(f, min_quality, max_quality)
    print(result)
    
def discrete_bisection_method(f: Callable, low: float, high: float):
    while high - low > 1:
        c = low + (high-low)//2
        if not (f(low) and f(c)):
            high = c
        elif not (f(c) and f(high)):
            low = c
    return high

def can_make_quality(quality: int, r: int, c: int, h: int, w: int, q: Matrix):
    acc_q_ones = prefix_sum_2d(r, c, q, quality)
    for i in range(r-h+1):
        for j in range(c-w+1):
            if rectangle_ones(i, j, h, w, acc_q_ones) < 0:
                return True
    return False

def prefix_sum_2d(r: int, c: int, q: Matrix, quality: int) -> Matrix:
    # c+1 and r+1: don't worry about the boundaries
    acc: Matrix = [[0]*(c+1) for _ in range(r+1)]
    for i in range(r):
        for j in range(c):
            m = 1 if q[i][j] > quality else -1
            acc[i+1][j+1] = m + acc[i+1][j] + acc[i][j+1] - acc[i][j]
    return acc

# Dynamic Programming
#
#         0 + 0 top_row-1 0 0 0
#         0 0 * * * * * * * * 0
# left_col-1 * * * * * * * right_col
#         0 0 * * * * * * * * 0
#         0 0 * bottom_row  + 0
#         0 0 0 0 0 0 0 0 0 0 0
def rectangle_ones(top_row: int, left_col: int, h: int, w: int, acc: Matrix):
    top_row += 1
    left_col += 1
    bottom_row = top_row + h - 1
    right_col = left_col + w - 1
    return (acc[bottom_row][right_col] 
            - acc[bottom_row][left_col-1] - acc[top_row-1][right_col] 
            + acc[top_row-1][left_col-1])