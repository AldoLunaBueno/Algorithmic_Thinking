# Problem: Promotion
# Judge: SPOJ
# ID: PRO

from typing import List
# from algorithms.brute_force import solve_by_brute_force
# from algorithms.heapq import solve_using_heapq
from algorithms.heapq_v2 import solve_using_heapq
import sys


def main():
    receipts = get_data()
    # solve_by_brute_force(receipts)
    solve_using_heapq(receipts)

def get_data() -> List[List[int]]:
    n = int(sys.stdin.readline().strip())
    receipts = []
    for _ in range(n):
        line = sys.stdin.readline()
        k, *day_receipts = line.split(" ")
        day_receipts = [int(r) for r in day_receipts]
        receipts.append(day_receipts)
    return receipts

if __name__ == "__main__":
    main()