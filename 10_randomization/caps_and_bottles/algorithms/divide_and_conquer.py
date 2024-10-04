from typing import List

# Resources: ---, 72.37 MB
# Final score: 60/100 (12.0/20 points)

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

    cap_piv = cap_arr[0]
    matching_bottle = 0

    for bottle_i in bottle_arr:
        print(f"0 {cap_piv} {bottle_i}")
        cap_vs_bottle = int(input().strip())        
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
        cap_vs_bottle = int(input().strip())
        if cap_vs_bottle < 0:
            caps_small.append(cap_i)
        elif cap_vs_bottle > 0:
            caps_big.append(cap_i)
    
    if len(caps_small) != 0:
        _recursion(caps_small, bottles_small)

    if len(caps_big) != 0:
        _recursion(caps_big, bottles_big)
        