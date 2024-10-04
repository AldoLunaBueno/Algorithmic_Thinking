# Quality of Living (Standard I/O)
# DMOJ problem ioi10p3

from typing import List
from sys import stdin
from algorithms.bisection_plus_dynamic_memory_friendly import solve

def main():
    r, c, h, w, q = get_data()
    solve(r, c, h, w, q)

def get_data():
    r, c, h, w = tuple((int(x) for x in stdin.readline().split(" ")))
    q = [[int(x) for x in stdin.readline().split(" ")] for _ in range(r)]
    stdin.close()
    return r, c, h, w, q

if __name__ == "__main__":
    main()
    
