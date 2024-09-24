# Lowest Price in Town
# UVa problem 10980

from typing import Any, List

MAX_DESIRED_NUM = 200

def main():
    cases = get_data()
    solve(cases)

class Case:
    def __init__(self, nums: List[int], prices: List[float], desires: List[int]) -> None:
        self.nums = nums
        self.prices = prices
        self.desires = desires

def solve(cases: List[Case]):
    for i in range(len(cases)):
        c: Case = cases[i]
        solve_k.clear()
        print("Case " + str(i+1) + ":")
        max_num = max(c.nums)
        for desired_num in c.desires:
            min_price = float("Inf")
            for offset in range(max_num): # at least k
                curr_price = solve_k(desired_num + offset, c.nums, c.prices)
                min_price = min_price if min_price < curr_price else curr_price
            print("Buy " + str(desired_num) + " for $" + "{:.2f}".format(min_price))

class Memoize:
    def __init__(self, func) -> None:
        self.func = func
        self.cache_array = [-1] * MAX_DESIRED_NUM
    def __call__(self, *args: Any, **kargs: Any) -> Any:
        k = args[0]
        if self.cache_array[k] == -1:
            self.cache_array[k] = self.func(*args, **kargs)
        return self.cache_array[k]
    def clear(self):
        self.cache_array = [-1] * MAX_DESIRED_NUM

@Memoize
def solve_k(desired_number: int, nums: List[int], prices: List[float]) -> float:
    """
    Returns the minimum total price for the exact "desired_number" of products
    """
    if desired_number == 0:
        return 0 # base case
    min_price = float("Inf")
    for i in range(len(nums)): # search options
        n = nums[i]
        if desired_number < n:
            continue
        total_price = solve_k(desired_number - n, nums, prices) + prices[i]
        min_price = min_price if min_price < total_price else total_price
    return min_price

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