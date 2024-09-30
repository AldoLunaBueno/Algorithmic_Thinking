# Yokan
# DMOJ problem dmpg15g6

# Resources: ---, 117.94 MB
# Final score: 60/100 (10.2/17 points)

from typing import List
from random import sample
from collections import defaultdict
from sys import stdin

MAX_ATTEMPTS = 7

def main():
    n, m, yokan, queries = get_data()
    solve(n, m, yokan, queries)

def get_data():
    all_data = stdin.read().split('\n')
    n, m = [int(x) for x in all_data[0].split(" ")]
    yokan = [0] + [int(x) for x in all_data[1].split(" ")]
    q = int(all_data[2])
    queries = [[int(x) for x in all_data[i].split(" ")] for i in range(3, q+3)]
    return n, m, yokan, queries

def solve(n, m, yokan, queries):
    pieces_by_flavor = defaultdict(list)
    for i, flavor in enumerate(yokan):
        pieces_by_flavor[flavor].append(i)
      
    for l, r in queries:
        width = r-l+1
        one_third = width/3
        happy_count = 0
        pieces_sample = sample(range(l, r+1), min(width, MAX_ATTEMPTS))
        rand_flavors = set([yokan[i] for i in pieces_sample])

        for flavor in rand_flavors:
            slab_by_flavor = pieces_by_flavor[flavor]
            one_flavor_width = flavor_range(l, r, slab_by_flavor)
            if one_flavor_width >= 2 * one_third:
                happy_count = 2
                break
            elif one_flavor_width >= one_third:
                happy_count += 1
                if happy_count == 2:
                    break

        print("YES" if happy_count == 2 else "NO")

def flavor_range(l, r, arr: List):
    li = binary_search(l, arr)
    if li == -1 or arr[li] < l:
        li += 1
    ri = binary_search(r, arr)
    return ri - li + 1

def binary_search(element, arr: List):
    low, high = -1, len(arr)
    while high - low > 1:
        mid = (low + high) // 2
        if arr[mid] > element:
            high = mid
        else:
            low = mid
    return low

if __name__ == "__main__":
    main()