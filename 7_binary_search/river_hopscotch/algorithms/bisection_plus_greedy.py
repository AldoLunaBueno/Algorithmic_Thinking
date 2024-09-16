from typing import Tuple, List, Callable

MAX_RIVER_WIDTH = 1_000_000_000
MAX_ROCKS = 50_000
ROCKS_TO_REMOVE = MAX_ROCKS

# Mindset transition from...
#   We must to calculate the max min jump directly
# to...
#   We can guess recursively (by bisection method) 
#   the max min jump 
#   and see (with greedy) if is feasible in m removes

def solve_by_bisection_plus_greedy(m: int, rocks: List[int]):
    rocks = sorted(rocks)
    f = lambda jump_guess: 1 if can_make_min_jump(jump_guess, m, rocks) else -1
    print(discrete_bisection_method(f, 0, MAX_RIVER_WIDTH))

def can_make_min_jump(jump_guess, m_removes, rocks: List[int]):
    n = len(rocks) # It's constant
    base = 0
    next = 1
    elimination_count = 0
    while next < n:
        while next < n and rocks[next] - rocks[base] < jump_guess:
            elimination_count += 1 # We don't remove anything really
            next += 1
        base = next
        next = base + 1

    return elimination_count <= m_removes # feasibility

def discrete_bisection_method(f: Callable, low: float, high: float, abs_tol = 1):
    if f(low) * f(high) > 0:
        Exception("Invalid interval")
    diff = high - low
    while diff > abs_tol:
        c = low + (high-low)//2
        if f(low) * f(c) < 0:
            high = c
        elif f(c) * f(high) < 0:
            low = c
        elif f(c) == 0:
            return c
        diff = high - low
    return low