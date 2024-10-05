# Knight Chase (A Knightly Pursuit)
# DMOJ problem ccc99s4

# problem related: https://dmoj.ca/problem/ccc10j5

from typing import List, Tuple

win = lambda moves: f"Win in {moves} knight move(s)."
loss = lambda moves: f"Loss in {moves} knight move(s)."
tie = lambda moves: f"Stalemate in {moves} knight move(s)."

def solve(cases: List):
    for (r, c, pr, pc, kr, kc) in cases:
        result = _solve_by_dp_plus_bfs(r, c, pr, pc, kr, kc)
        print(result)

def _solve_by_dp_plus_bfs(r, c, pr, pc, kr, kc):
    if pr == r:
        return loss(0)
    if kc == pc and kr == pr + 1:
        return tie(0)
    
    # dynamic programming and bfs
    board = fill_min_board(r, c, kr, kc)
    
    for j in range(1, r-pr+1):
        if j == board[pc][pr+j]:
            return win(j)
        
    if r == pr+1:
        return loss(1)

    for j in range(1, r-pr):
        if j == board[pc][pr+j+1]:
            return tie(j)
    
    return loss(r-pr-1)

def fill_min_board(r, c, kr, kc):
    N = r * c
    board = [[N]*(r+1) for _ in range(c+1)]
    num_moves = 0
    board[kc][kr] = num_moves
    visited = [(kc, kr)]        
    while True:
        num_moves = num_moves + 1
        next_to_visit = []
        for from_position in visited:
            for i, j in moves(from_position, c, r):
                if num_moves < board[i][j]:
                    board[i][j] = num_moves
                    next_to_visit.append((i,j))
        visited = next_to_visit
        if len(visited) == 0:
            break
    return board

def moves(from_position: Tuple, c, r):
    i, j = from_position
    all_moves = [
        (i+1, j+2), (i+2, j+1),
        (i-1, j-2), (i-2, j-1),
        (i+2, j-1), (i+1, j-2),
        (i-2, j+1), (i-1, j+2)
    ]
    result = [(i, j) for i, j in all_moves
              if (1 <= i <= c) and (1 <= j <= r)]
    return result

def main():
    cases = get_data()
    solve(cases)

def get_data():
    n = int(input())
    cases = []
    for _ in range(n):
        r =  int(input())
        c =  int(input())
        pr = int(input())
        pc = int(input())
        kr = int(input())
        kc = int(input())
        cases.append((r, c, pr, pc, kr, kc))
    return cases
        

if __name__ == "__main__":
    main()