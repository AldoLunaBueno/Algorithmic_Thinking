from typing import List, Callable
Matrix = List[List[int]]

# Resources: 6.761s, 289.61 MB
# Final score: 80/100 (12.0/15 points)

# main() function was optimized with sys.stdin.readline() 
# instead of input() built-in function

def solve(r: int, c: int, h: int, w: int, q: Matrix):
    min_quality = h*w//2
    max_quality = r*c + 1 - h*w//2
    f = lambda x: 1 if can_make_quality(x, r, c, h, w, q) else -1
    result = discrete_bisection_method(f, min_quality, max_quality)
    print(result)
    
def discrete_bisection_method(f: Callable, low: float, high: float):
    abs_tol = 1
    if f(low) * f(high) >= 0:
        raise Exception("Bad interval")
    while high - low > abs_tol:
        c = low + (high-low)//2
        if f(low) * f(c) < 0:
            high = c
        elif f(c) * f(high) < 0:
            low = c
        elif f(c) == 0:
            return c
    return high

def can_make_quality(quality: int, r: int, c: int, h: int, w: int, q: Matrix):
    q_ones = [[-1 if q_value <= quality else 1
               for q_value in row] for row in q]
    acc_q_ones = prefix_sum_2d(r, c, q_ones)
    for i in range(r-h+1):
        for j in range(c-w+1):
            if rectangle_ones(i, j, h, w, acc_q_ones) < 0:
                return True
    return False

def prefix_sum_2d(r: int, c: int, matrix: Matrix) -> Matrix:
    # c+1 and r+1: don't worry about the boundaries
    acc: Matrix = [[0]*(c+1) for _ in range(r+1)]
    for i in range(r):
        for j in range(c):
            acc[i+1][j+1] = matrix[i][j] + acc[i+1][j] + acc[i][j+1] - acc[i][j]
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