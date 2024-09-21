from typing import List, Tuple

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

def solve_t(m, n, t):
    dp = [0]*(t+1)
    for i in range(1, t+1):
        first =  dp[i-m] if i >= m else -1
        second = dp[i-n] if i >= n else -1
        if first == -1 and second == -1:
            dp[i] = -1
        else:
            dp[i] = max(first, second) + 1
    return dp