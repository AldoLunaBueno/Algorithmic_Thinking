# Resources: 0.443s, 12.28 MB
# Final score: 10/25 (4.0/10 points)
def solve(n, outcome_1, points_1, outcome_2, points_2):
    solve_i_j.clear()
    result = solve_i_j(n-1, n-1, outcome_1, points_1, outcome_2, points_2)
    print(result)

class Memoize:
    def __init__(self, func) -> None:
        self.func = func
        self.cache = {}
    def __call__(self, *args, **kargs):
        key = (args[0], args[1])
        if key not in self.cache:
            self.cache[key] = self.func(*args, **kargs)
        return self.cache[key]
    def clear(self):
        self.cache.clear()

@Memoize
def solve_i_j(i, j, outcome_1, points_1, outcome_2, points_2):
    if i == -1 or j == -1: # this simplifies all
        return 0
    
    option_1 = 0 # rivalry game and team 1 and 2 move
    if ((outcome_1[i] == "W" and outcome_2[j] == "L" and points_1[i] > points_2[j]) or
        (outcome_1[i] == "L" and outcome_2[j] == "W" and points_1[i] < points_2[j])):
        option_1 = points_1[i] + points_2[j]
        option_1 += solve_i_j(i-1, j-1, outcome_1, points_1, outcome_2, points_2)
    # team 1 move
    option_2 = solve_i_j(i-1, j, outcome_1, points_1, outcome_2, points_2)
    # team 2 move
    option_3 = solve_i_j(i, j-1, outcome_1, points_1, outcome_2, points_2)

    return max(option_1, option_2, option_3)