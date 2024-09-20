from typing import List, Tuple
from functools import wraps

def solve(cases: List[Tuple[int]]):
    for (m, n, t) in cases:
        t_max = t
        burgers = 0
        while t_max >= 0:
            burgers = solve_t(m, n, t_max)
            if burgers != -1:
                break
            t_max -= 1
        
        beer_time = t-t_max
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

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kargs):
        key = str(args)
        if key not in cache:
            cache[key] = func(*args, **kargs)
        return cache[key]
    return wrapper

@memoize
def solve_t(m: int, n: int, t: int):
    if t == 0:
        return 0 # base case
    
    first =  solve_t(m, n, t-m) if t >= m else -1
    second = solve_t(m, n, t-n) if t >= n else -1

    if first == -1 and second == -1:
        return -1 # fail
    else:
        return max(first, second) + 1