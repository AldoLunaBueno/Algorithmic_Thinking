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


Problema de llamar la función main desde el test para probar un script

if __name__ == "__main__":
    main()

def _test_from_data(capsys: pytest.CaptureFixture[str], input_data, expected):
    # Sets standard input (sys.stdin)
    sys.stdin = io.StringIO(input_data)
    
    main() # method to be tested

    # Capture the output
    out, err = capsys.readouterr()
    
    # Compare the output with the expected result
    assert out.strip() == expected

Esta es la solución: usar el módulo subprocess

    result = subprocess.run(
        [sys.executable, # get the current Python interpreter
         path_to_script],
        input=input_data,
        text=True,
        capture_output=True
    )
    out = result.stdout.strip()


# My 1 hour error was due to relying on data cleanliness
# The strip() safed the day
text = [input().strip() for _ in range(m)]




# The next multisort works because the sort stability 
# of the build-in sorted() method:

# sort on secondary key
nodes = sorted(nodes, key = lambda node: node.name)
# sort on primary key
nodes = sorted(nodes, key = lambda node: node.score, reverse=True)