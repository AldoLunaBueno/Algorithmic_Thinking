# Yokan
# DMOJ problem dmpg15g6

# Resources: 11.375s, 120.75 MB
# Maximum single-case runtime: 1.202s
# Final score: 100/100 (17.0/17 points)

from typing import List
from collections import defaultdict, Counter
from sys import stdin
from bisect import bisect_left, bisect_right

SAMPLE_SIZE = 30
MAX_ATTEMPTS = 3

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
        step = max((r-l+1) // min(width, SAMPLE_SIZE), 1)
        pieces_sample = range(l, r+1, step)
        counter = Counter([yokan[i] for i in pieces_sample])

        for flavor, _ in counter.most_common(MAX_ATTEMPTS):
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
    li = bisect_left(arr, l)
    ri = bisect_right(arr, r)
    return ri - li

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