from typing import List

# Resources: ---, 262.95 MB
# Final score: 40/100 (6.0/15 points)
def solve(r: int, c: int, h: int, w: int, q: List[List[int]]):
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