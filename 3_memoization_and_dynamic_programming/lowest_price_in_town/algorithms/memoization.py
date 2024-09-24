from functools import wraps
from typing import List
from case_class import Case

def solve(cases: List[Case]):
    for i in range(len(cases)):
        c: Case = cases[i]
        solve_k_memo = memoize(solve_k)
        print("Case " + str(i+1) + ":")
        max_num = max(c.nums)
        for desired_num in c.desires:
            min_price = float("Inf")
            for offset in range(max_num): # at least k
                curr_price = solve_k_memo(desired_num + offset, c.nums, c.prices)
                min_price = min_price = min(min_price, curr_price)
            print("Buy " + str(desired_num) + " for $" + "{:.2f}".format(min_price))

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
        p = prices[i]
        total_price = solve_k(desired_number - n, nums, prices) + p
        min_price = min(min_price, total_price)
    return min_price

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kargs):
        k, *_ = args
        key = str(k)
        if key not in cache:
            cache[key] = func(*args, **kargs)
        return cache[key]
    return wrapper


    

    