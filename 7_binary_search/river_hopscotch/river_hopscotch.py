# River Hopscotch
# POJ problem 3258

from typing import Tuple, List
from algorithms.bisection_plus_greedy import solve_by_bisection_plus_greedy


MAX_RIVER_WIDTH = 1_000_000_000
MAX_ROCKS = 50_000
ROCKS_TO_REMOVE = MAX_ROCKS

def main():
    m, rocks = get_data()
    solve_by_bisection_plus_greedy(m, rocks)

def get_data() -> Tuple[List[int], int]:
    L, n, m = [int(x) for x in input().split(" ")]
    rocks = [0]
    for _ in range(n):
        rocks.append(int(input()))
    rocks.append(L)
    return m, rocks

if __name__ == "__main__":
    main()