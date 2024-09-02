from typing import List

def main():
    q, queries = get_data()
    solve_by_naive()

def get_data():
    q = int(input())
    queries: List[str] = [None] * q
    for i in range(q):
        queries[i] = input()
    queries = [query.split(" ") for query in queries]
    queries = [(int(query[0]), query[1]) for query in queries]
    return q, queries

def solve_by_naive():
    pass

if __name__ == "__main__":
    main()