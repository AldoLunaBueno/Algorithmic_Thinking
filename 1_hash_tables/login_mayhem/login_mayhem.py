from typing import List, Tuple

def main():
    q, queries = get_data()
    solve_by_naive(q, queries)

def get_data() -> Tuple[int, List[Tuple[int, str]]]:
    q = int(input())
    queries: List[str] = [None] * q
    for i in range(q):
        queries[i] = input()
    queries = [query.split(" ") for query in queries]
    queries = [(int(query[0]), query[1]) for query in queries]
    return q, queries

# TIME: O(**2)
def solve_by_brute_force(q: int, queries: List[Tuple[int, str]]):
    pass_db = [] # database of passwords
    for query in queries: # time: O(n**2)
        pass_user = query[1]

        if query[0] == 1:
            pass_db.append(pass_user)
            continue

        # query[0] == 2
        violation_count = 0
        for p in pass_db: # time: O(n)
            if pass_user in p:
                violation_count += 1
        print(f"{violation_count}")

if __name__ == "__main__":
    main()