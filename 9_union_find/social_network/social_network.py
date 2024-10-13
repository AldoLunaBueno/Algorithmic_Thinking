# Social Network Community
# SPOJ problem SOCNETC

from algorithms.union_find import solve


def main():
    n, m, q = get_data()
    solve(n, m, q)

def get_data():
    n, m = [int(x) for x in input().split(" ")]
    num_q = int(input())
    q = []
    for _ in range(num_q):
        command, *args = input().split(" ")
        args = [int(x) for x in args]
        q.append((command, *args))
    return n, m, q

if __name__ == "__main__":
    main()

