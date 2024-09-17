# Quality of Living (Standard I/O)
# DMOJ problem ioi10p3

from typing import List


def main():
    r, c, h, w, q = get_data()
    solve_by_brute_force(r, c, h, w, q)

def get_data():
    q: List[List[int]] = []
    r, c, h, w = [int(x) for x in input().split(" ")]    
    for _ in range(r):
        row = [int(x) for x in input().split(" ")]
        q.append(row)
    return r, c, h, w, q

# Resources: ---, 262.95 MB
# Final score: 40/100 (6.0/15 points)
def solve_by_brute_force(r: int, c: int, h: int, w: int, q: List[List[int]]):
    best = float("Inf")
    for i in range(r-h+1):
        for j in range(c-w+1):
            arr = rectangle(i, j, h, w, q)
            m = median(arr)
            if m < best:
                best = m
    print(best)

def median(a: List[int]):
    a = sorted(a)
    n = len(a)
    return a[n//2]

def rectangle(i: int, j: int, h: int, w: int, q: List[List[int]]):
    acc = []
    for i0 in range(h):
        acc.extend(q[i+i0][j:j+w])
    return acc

if __name__ == "__main__":
    main()
    
