import sys
import resource
resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
sys.setrecursionlimit(0x100000)

def main():
    cases = get_data()
    solve(cases)
def solve(cases):
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
    def wrapper(*args, **kargs):
        key = str(args)
        if key not in cache:
            cache[key] = func(*args, **kargs)
        return cache[key]
    return wrapper
@memoize
def solve_t(m, n, t):
    if t == 0:
        return 0
    first = solve_t(m, n, t-m) if t >= m else -1
    second = solve_t(m, n, t-n) if t >= n else -1
    if first == -1 and second == -1:
        return -1
    else:
        maximum = first if first > second else second
        return maximum + 1
def get_data():
    cases = []
    while True:
        try:
            one_case = tuple(int(x) for x in input().split(" "))
            cases.append(one_case)
        except EOFError:
            break
    return cases
if __name__ == "__main__":
    main()