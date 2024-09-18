# Quality of Living (Standard I/O)
# DMOJ problem ioi10p3

from typing import List
from algorithms.bisection_plus_dinamic import solve

def main():
    r, c, h, w, q = get_data()
    solve(r, c, h, w, q)

def get_data():
    q: List[List[int]] = []
    r, c, h, w = [int(x) for x in input().split(" ")]    
    for _ in range(r):
        row = [int(x) for x in input().split(" ")]
        q.append(row)
    return r, c, h, w, q

if __name__ == "__main__":
    main()
    
