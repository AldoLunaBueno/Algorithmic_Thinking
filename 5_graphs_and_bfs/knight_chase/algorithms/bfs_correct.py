from typing import List, Tuple

win = lambda moves: f"Win in {moves} knight move(s)."
loss = lambda moves: f"Loss in {moves} knight move(s)."
tie = lambda moves: f"Stalemate in {moves} knight move(s)."

def solve(cases: List):
    for (r, c, pr, pc, kr, kc) in cases:
        result = _solve_by_dp_plus_bfs(r, c, pr, pc, kr, kc)
        print(result)

def _solve_by_dp_plus_bfs(r, c, pr, pc, kr, kc):
    pawn_takes = r - pr
    if pawn_takes <= 1:
        return loss(0)
    if kc == pc and kr == pr + 1:
        return tie(0)
    
    board = fill_min_board(r, c, kr, kc)
    
    for j in range(1, pawn_takes):
        knight_takes = board[pc][pr+j]
        if 0 <= knight_takes <= j and (j - knight_takes) % 2 == 0:
            return win(j)

    for j in range(1, pawn_takes):
        knight_takes = board[pc][pr+j+1]
        if 0 <= knight_takes <= j and (j - knight_takes) % 2 == 0:
            return tie(j)
    
    return loss(pawn_takes-1)

# bfs (like dynamic programming)
def fill_min_board(r, c, kr, kc):
    board = [[-1]*(r+1) for _ in range(c+1)]
    num_moves = 0
    board[kc][kr] = num_moves
    visited = [(kc, kr)]        
    while True:
        num_moves = num_moves + 1
        next_to_visit = []
        for from_position in visited:
            for i, j in moves(from_position, c, r):
                if board[i][j] == -1:
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