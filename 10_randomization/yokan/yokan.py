# Yokan
# DMOJ problem dmpg15g6

# Resources: ---, 61.64 MB
# Final score: 60/100 (10.2/17 points)

from typing import List
from math import ceil
from random import sample
from functools import wraps
from collections import defaultdict

MAX_ATTEMPTS = 20

def main():
    n, m, yokan, queries = get_data()
    solve(n, m, yokan, queries)

def get_data():
    n, m = [int(x) for x in input().strip().split(" ")]
    yokan = [0] + [int(x) for x in input().strip().split(" ")]
    q = int(input())
    queries = []
    for _ in range(q):
        query = [int(x) for x in input().strip().split(" ")]
        queries.append(query)
    return n, m, yokan, queries

def solve(n, m, yokan, queries):
    pieces_by_flavor = defaultdict(list)
    for i, flavor in enumerate(yokan):
        pieces_by_flavor[flavor].append(i)
      
    for l, r in queries:
        width = r-l+1
        one_third = ceil(width/3)
        two_third = ceil(2*width/3)
        happy_count = 0
        pieces_sample = sample(range(l, r+1), min(width, MAX_ATTEMPTS))
        rand_flavors = set([yokan[i] for i in pieces_sample])

        for flavor in rand_flavors:
            slab_by_flavor = pieces_by_flavor[flavor]
            li = binary_search(slab_by_flavor, l, to_right=True)
            ri = binary_search(slab_by_flavor, r)  
            one_flavor_width = ri-li+1
            if one_flavor_width >= two_third:
                happy_count = 2
            elif one_flavor_width >= one_third:
                happy_count += 1
            if happy_count == 2:
                break

        print("YES" if happy_count == 2 else "NO")

def binary_search(arr: List, element, to_right=False):
    low, high = -1, len(arr)
    while high - low > 1:
        mid = (low + high) // 2
        if arr[mid] > element:
            high = mid
        else:
            low = mid
    if to_right and (low == -1 or arr[low] < element):
        return low + 1
    return low

if __name__ == "__main__":
    main()