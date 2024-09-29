# Yokan
# DMOJ problem dmpg15g6

from typing import List, Callable

def main():
    n, m, flavor_of_pieces, queries = get_data()
    solve(n, m, flavor_of_pieces, queries)

def get_data():
    n, m = [int(x) for x in input().strip().split(" ")]
    flavor_of_pieces = [int(x) for x in input().strip().split(" ")]
    q = int(input())
    queries = []
    for _ in range(q):
        query = [int(x) for x in input().strip().split(" ")]
        queries.append(query)
    return n, m, flavor_of_pieces, queries

def solve(n, m, flavor_of_pieces, queries):
    flavors_by_piece: List[List[int]] = [None] * (m+1)
    for i, flavor in enumerate(flavor_of_pieces):
        if flavors_by_piece[flavor] == None:
            flavors_by_piece[flavor] = []
        flavors_by_piece[flavor].append(i)
    for flavors in flavors_by_piece:
        print(flavors)
    
    # Get pieces of the flavor 1 in the slab 1 defined by r and l limits:
    flavor_selected = 1
    r = 3
    l = 10
    a = flavors_by_piece[1]
    r_i = binary_search(a, r)
    l_i = binary_search(a, l)    
    print(a[r_i:l_i]) # Result!!

def binary_search(arr: List, element):
    f = lambda index: 1 if arr[index] > element else -1
    return 1 + discrete_bisection_method(f, 0, len(arr)-1)

def discrete_bisection_method(f: Callable, low: float, high: float, abs_tol = 1):
    if f(low) * f(high) > 0:
        Exception("Invalid interval")
    diff = high - low
    while diff > abs_tol:
        c = low + (high-low)//2
        if f(low) * f(c) < 0:
            high = c
        elif f(c) * f(high) < 0:
            low = c
        elif f(c) == 0:
            return c
        diff = high - low
    return low

if __name__ == "__main__":
    main()