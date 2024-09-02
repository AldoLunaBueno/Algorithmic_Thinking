from typing import List, Tuple

def main():
    q, queries = get_data()
    solve_by_hash_table(q, queries)

# TIME: O(n**2)
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
        print(violation_count)

# TIME: O(n)
def solve_by_hash_table(q: int, queries: List[Tuple[int, str]]):
    hash_table = {}
    for query in queries: # time: O(100*n) = O(n)
        pass_user = query[1]
        
        if query[0] == 1:
            all_subs = _get_subs(pass_user) # time: O(100)
            for s in all_subs: # time: O(100)
                if s not in hash_table:
                    hash_table[s] = 1
                else:
                    hash_table[s] += 1
            continue

        violation_count = 0
        if pass_user in hash_table:
            violation_count = hash_table[pass_user] # O(1)
        print(violation_count)
            
        

def _get_subs(s: str) -> List[str]:
    if len(s) == 1:
        return [s]
    
    subs = []
    for start in range(len(s)):
        for end in range(start+1, len(s)+1):
            subs.append(s[start:end])
    
    return list(set(subs))

def get_data() -> Tuple[int, List[Tuple[int, str]]]:
    q = int(input())
    queries: List[str] = [None] * q
    for i in range(q):
        queries[i] = input()
    queries = [query.split(" ") for query in queries]
    queries = [(int(query[0]), query[1]) for query in queries]
    return q, queries

if __name__ == "__main__":
    main()