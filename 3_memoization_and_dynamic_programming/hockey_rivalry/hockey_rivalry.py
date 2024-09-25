# Geese vs. Hawks (Hockey Rivalry)
# DMOJ problem cco18p1

from algorithms.dynamic_prog import solve

def main():
    n, outcome_1, points_1, outcome_2, points_2 = get_data()
    solve(n, outcome_1, points_1, outcome_2, points_2)

def get_data():
    n = int(input())
    outcome_1 = input()
    points_1 = [int(x) for x in input().split(" ")]
    outcome_2 = input()
    points_2 = [int(x) for x in input().split(" ")]
    return n, outcome_1, points_1, outcome_2, points_2

if __name__ == "__main__":
    main()