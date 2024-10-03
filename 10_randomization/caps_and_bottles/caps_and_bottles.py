# Caps and Bottles (Bottle Caps)
# DMOJ problem cco09p4

from algorithms.brute_force import solve


def main():
    n = get_data()
    solve(n)

def get_data():
    n = int(input().strip())
    return n


if __name__ == "__main__":
    main()