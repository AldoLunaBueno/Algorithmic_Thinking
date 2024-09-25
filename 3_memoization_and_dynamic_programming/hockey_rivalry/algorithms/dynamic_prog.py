from typing import List

# Resources: 3.253s, 52.88 MB
# Maximum single-case runtime: 0.577s
# Final score: 25/25 (10.0/10 points)
def solve(n: int, outcome_1: List, points_1: List, outcome_2: List, points_2: List):    
    result = solve_dp(n, outcome_1, points_1, outcome_2, points_2)
    print(result)

def solve_dp(n: int, outcome_1: List, points_1: List, outcome_2: List, points_2: List):
    zeros = [0] * (n+1)
    dp = [zeros[:] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            option_1 = 0 # rivalry game and team 1 and 2 last game
            if ((outcome_1[i-1] == "W" and outcome_2[j-1] == "L" and points_1[i-1] > points_2[j-1]) or
                (outcome_1[i-1] == "L" and outcome_2[j-1] == "W" and points_1[i-1] < points_2[j-1])):
                option_1 = points_1[i-1] + points_2[j-1]
                option_1 += dp[i-1][j-1]
            option_2 = dp[i-1][j] # team 1 previous game
            option_3 = dp[i][j-1] # team 2 previous game
            dp[i][j] = max(option_1, option_2, option_3)
    return dp[n][n]