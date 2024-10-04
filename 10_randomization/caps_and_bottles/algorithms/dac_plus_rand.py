# Resources: 51.152s, 70.19 MB
# Maximum single-case runtime: 6.869s
# Final score: 100/100 (20.0/20 points)

# The key optimization to pass all the test cases of the judge 
# was use stdin.readline() instead of input().
# My test script now is capable of test this withouth crash.

from typing import List
from random import choice
from sys import stdin

# Time complexity: O(n*log(n))
def solve(n: int):
    cap_indexes = range(1, n+1)
    bottle_indexes = range(1, n+1)
    _recursion(cap_indexes, bottle_indexes)

def _recursion(cap_arr: List[int], bottle_arr: List[int]):    
    caps_big = []
    caps_small = []
    bottles_big = []
    bottles_small = []

    cap_piv = choice(cap_arr)
    matching_bottle = 0

    for bottle_i in bottle_arr:
        print(f"0 {cap_piv} {bottle_i}")
        cap_vs_bottle = int(stdin.readline().strip())
        if cap_vs_bottle < 0:
            bottles_big.append(bottle_i)
        elif cap_vs_bottle > 0:
            bottles_small.append(bottle_i)
        elif cap_vs_bottle == 0:
            print(f"1 {cap_piv} {bottle_i}")
            matching_bottle = bottle_i
    
    for cap_i in cap_arr:
        if cap_i == cap_piv: # query already done
            continue
        print(f"0 {cap_i} {matching_bottle}")
        cap_vs_bottle = int(stdin.readline().strip())
        if cap_vs_bottle < 0:
            caps_small.append(cap_i)
        elif cap_vs_bottle > 0:
            caps_big.append(cap_i)
    
    if len(caps_small) != 0:
        _recursion(caps_small, bottles_small)

    if len(caps_big) != 0:
        _recursion(caps_big, bottles_big)