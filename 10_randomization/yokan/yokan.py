# Yokan
# DMOJ problem dmpg15g6

# Resources: ---, 61.64 MB
# Final score: 40/100 (6.8/17 points)

from typing import List, Callable
from math import ceil
from random import randint

MAX_ATTEMPTS = 60

def main():
    n, m, yokan, queries = get_data()
    solve(n, m, yokan, queries)

def get_data():
    n, m = [int(x) for x in input().strip().split(" ")]
    yokan = [None] + [int(x) for x in input().strip().split(" ")]
    q = int(input())
    queries = []
    for _ in range(q):
        query = [int(x) for x in input().strip().split(" ")]
        queries.append(query)
    return n, m, yokan, queries

def solve(n, m, yokan, queries):
    pieces_by_flavor: List[List[int]] = [None] * (m+1)
    for i, flavor in enumerate(yokan):
        if flavor == None:
            continue
        if pieces_by_flavor[flavor] == None:
            pieces_by_flavor[flavor] = []
        pieces_by_flavor[flavor].append(i)
      
    for l, r in queries:
        width = r-l+1
        one_third = ceil(width/3)
        two_third = ceil(2*width/3)
        happy_count = 0
        flavors_tried = set()

        for _ in range(MAX_ATTEMPTS):
            rand_piece = randint(l, l+width-1)
            flavor = yokan[rand_piece]
            slab_by_flavor = pieces_by_flavor[flavor]

            if len(flavors_tried) == m:
                break
            elif flavor in flavors_tried:
                continue
            
            flavors_tried.add(flavor)

            li = binary_search(slab_by_flavor, l, high=True)
            ri = binary_search(slab_by_flavor, r)  
            one_flavor_width = ri-li+1
            if one_flavor_width >= two_third:
                happy_count = 2
            elif one_flavor_width >= one_third:
                happy_count += 1
            
            if happy_count == 2:
                break

        print("YES" if happy_count == 2 else "NO")

def binary_search(arr: List, element, high = False):
    if element < arr[0]:
        return 0 if high else -1
    if element > arr[-1]:
        return len(arr) if high else len(arr)-1

    def f(index): 
        if arr[index] > element:
            return 1
        elif arr[index] < element:
            return -1
        else:
            return 0
    if high:
        i = discrete_bisection_method(f, 0, len(arr)-1)
        if arr[i] < element:
            return i+1
        else:
            return i
    return discrete_bisection_method(f, 0, len(arr)-1)

def discrete_bisection_method(f: Callable, low: int, high: int):
    if f(low) * f(high) > 0:
        Exception("Invalid interval")
    if f(low) == 0:
        return low
    if f(high) == 0:
        return high
    diff = high - low
    while diff > 1:
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