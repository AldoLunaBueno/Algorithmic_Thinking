# Problem: Snowflakes
# Judge: DMOJ 
# ID: cco07p2

from typing import List
from solve_algorithms.hash_table import HashTableAlgorithm
# from solve_algorithms.naive import NaiveAlgorithm
from standard_comparator import StandardComparator

def main():
    n, n_lines = get_data()

    comparator = StandardComparator()
    # solver = NaiveAlgorithm(comparator)
    solver = HashTableAlgorithm(comparator)
    solver.solve(n, n_lines)

def get_data():
    n = int(input())
    n_lines = []
    for _ in range(n):
        line = input()
        line = line.split(" ")
        line = [int(x) for x in line]
        n_lines.append(line)
    return n, n_lines

if __name__ == "__main__":
    main()