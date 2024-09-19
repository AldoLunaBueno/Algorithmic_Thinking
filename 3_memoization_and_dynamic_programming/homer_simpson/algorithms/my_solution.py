from functools import wraps
from typing import List, Tuple

def solve(cases):
    for (m, n, t) in cases:
        burger_numb, t0 = _solve(m, n, t)
        if t0 == t:
            print(burger_numb)
        else:
            print(str(burger_numb) + " " + str(t-t0))

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
def _solve(m: int, n: int, t: int):
    if t == 0:
        return 0, 0
    if m > n:
        m, n = n, m
    m_numb = t // m
    m_r = t % m
    if m_r == 0:
        return m_numb, t
    m_time = m * m_numb
    while m_time >= 0:            
        if (t - m_time) % n == 0:
            n_numb = (t - m_time) // n
            return m_numb + n_numb, t
        m_time -= m
        m_numb -= 1
    return _solve(m, n, t-1)
        