# Knight Chase (A Knightly Pursuit)
# DMOJ problem ccc99s4

# problem related: https://dmoj.ca/problem/ccc10j5

from algorithms.bfs_correct import solve

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