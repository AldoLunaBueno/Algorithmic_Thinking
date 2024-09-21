from typing import List, Tuple
from functools import wraps

def solve(cases: List[Tuple[int]]):
    for (m, n, t) in cases:
        dp = solve_t(m, n, t)
        i = t
        burgers = dp[i]
        while burgers == -1:
            i -= 1
            burgers = dp[i]
        
        beer_time = t-i
        if beer_time == 0:
            if burgers == 0:
                print(0)
            else:
                print(burgers)
        else:
            if burgers == 0:
                print("0 " + str(beer_time))
            else:
                print(str(burgers) + " " + str(beer_time))

def memoize_for_solve_t(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        m, n, t = args
        key = str((m, n))
        key_rev = str((n, m))
        if key not in cache:
            cache[key] = func(*args)
            cache[key_rev] = cache[key]
        if t+1 > len(cache[key]):
            cache[key] = func(*args, memo_dp = cache[key])
            cache[key_rev] = cache[key]
        return cache[key]
    return wrapper

@memoize_for_solve_t
def solve_t(m, n, t, memo_dp: List[int] = None):
    if memo_dp == None:
        memo_dp = [0]
    dp = memo_dp
    i0 = len(memo_dp)
    dp.extend([0]*(t+1-i0))
    
    for i in range(i0, t+1):
        first =  dp[i-m] if i >= m else -1
        second = dp[i-n] if i >= n else -1
        if first == -1 and second == -1:
            dp[i] = -1
        else:
            dp[i] = max(first, second) + 1
    return dp