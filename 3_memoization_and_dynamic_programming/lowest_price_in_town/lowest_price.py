# Lowest Price in Town
# UVa problem 10980

from typing import List
from case_class import Case
from algorithms.memoization import solve
def main():
    cases = get_data()
    solve(cases)

def get_data():
    cases: List[Case] = []  
    while True:
        nums: List[int] = []
        prices: List[float] = []
        desires: List[int] = []        
        try:
            header = input()
        except EOFError:
            break
        unit_price, m = header.split(" ")
        unit_price = float(unit_price)
        m = int(m)
        nums.append(1)
        prices.append(unit_price)
        for _ in range(m):
            n, p = input().split(" ")
            n = int(n)
            p = float(p)
            nums.append(n)
            prices.append(p)
        desires = [int(k) for k in input().split(" ")]
        c = Case(nums, prices, desires)
        cases.append(c)
    return cases

if __name__ == "__main__":
    main()