# Resources: 2.250s, 100.77 MB
# Maximum single-case runtime: 0.270s
# Final score: 27/27 (12.0/12 points)

from typing import List, Tuple

NON_VISITED = -1 # non visited heights are -1
OBSTACLE = float("Inf") # visited heights and obstacles are >= 0

def solve(target_height: int, jump: int, itching_powder: List[Tuple]):
    rope = [NON_VISITED]*(target_height + jump)
    for a, b in itching_powder:
        for i in range(a, b+1):
            rope[i] = OBSTACLE
    num_jumps = 0
    rope[0] = num_jumps

    # bfs
    visited = [0]
    full_height = 0 # height up to which the rope has been fully visited
        # it's an ad-hoc limit to avoid move down to visited heights
    while len(visited) != 0:
        num_jumps += 1
        next_to_visit = []
        for from_height in visited:           
            for to_height in moves(from_height, jump, rope, full_height):
                if to_height >= target_height:
                    print(num_jumps)
                    return
                rope[to_height] = num_jumps
                next_to_visit.append(to_height)
            if full_height < from_height:
                full_height = from_height
        visited = next_to_visit
    
    print(-1)

def moves(from_height: int, jump: int, rope: List[int], full_height: int) -> List[int]:
    fall_heights = [to_height for to_height in range(full_height, from_height) 
            if rope[to_height] == NON_VISITED]
    if rope[from_height + jump] == NON_VISITED:
        return fall_heights + [from_height + jump]
    return fall_heights