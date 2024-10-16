# Drawer Chore (Ladice)
# DMOJ problem coci13c5p6

from algorithms.my_way import solve

def main():
    n, d, pairs = get_data()
    solve(n, d, pairs)

def get_data():
    n, d = [int(x) for x in input().split(" ")]
    pairs = []
    for _ in range(n):
        d1, d2 = [int(x) for x in input().split(" ")]
        pairs.append((d1, d2))
    return n, d, pairs

if __name__ == "__main__":
    main()