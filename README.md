# Algorithmic_Thinking


cases = []
    while True:
        try:
            one_case = tuple(int(x) for x in input().split(" "))
            cases.append(one_case)
        except EOFError:
            break
    return cases

RecursionError: maximum recursion depth exceeded while getting the str of an object

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