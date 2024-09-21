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