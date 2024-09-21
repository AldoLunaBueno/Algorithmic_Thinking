# Homer Simpson (Burger Fever)
# UVa problem 10465

from algorithms.memo_and_dynamic import solve

def main():
    cases = get_data()
    solve(cases)

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