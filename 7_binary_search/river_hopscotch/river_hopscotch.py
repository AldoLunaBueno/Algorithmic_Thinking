# River Hopscotch
# POJ problem 3258

from typing import Tuple, List

MAX_RIVER_WIDTH = 1_000_000_000
MAX_ROCKS = 50_000
ROCKS_TO_REMOVE = MAX_ROCKS

def main():
    m, rocks = get_data()
    solve_by_greedy(m, rocks)

def get_data() -> Tuple[List[int], int]:
    L, n, m = [int(x) for x in input().split(" ")]
    rocks = [0]
    for _ in range(n):
        rocks.append(int(input()))
    rocks.append(L)
    return m, rocks

def solve_by_greedy(m: int, rocks: List[int]):
    rocks = sorted(rocks)
    min_jump = float("Inf")
    
    for _ in range(m):
        min_jump, min_index = get_min_jump(rocks)
        if min_index == 0:
            rocks.pop(min_index+1)
            continue
        elif min_index == len(rocks)-2:
            rocks.pop(min_index)
            continue
        
        neighbor_1 = rocks[min_index] - rocks[min_index-1]
        neighbor_2 = rocks[min_index+2] - rocks[min_index+1]
        if neighbor_1 < neighbor_2:
            rocks.pop(min_index)
        else:
            rocks.pop(min_index+1)

    min_jump, _ = get_min_jump(rocks)
    print(min_jump)

def get_min_jump(rocks):
    n = len(rocks)
    min_jump = float("Inf")
    min_index = -1        
    for i in range(n-1):
        jump = rocks[i+1] - rocks[i]
        if jump < min_jump:
            min_jump = jump
            min_index = i
    return min_jump, min_index

if __name__ == "__main__":
    main()