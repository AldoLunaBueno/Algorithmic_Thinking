from algorithms.dijkstra import solve

def main():
    cases = get_data()
    solve(cases)


def get_data():
    num_test_cases = int(input())
    cases = []
    for _ in range(num_test_cases):
        _ = input()
        n = int(input()) # number of cells
        e = int(input()) # exit cell
        t = int(input()) # limit time for mice to exit
        m = int(input()) # number of passages between cells
        passages = []
        for _ in range(m):
            passage = [int(x) for x in input().split(" ")]
            passages.append(passage)
        cases.append((n, e, t, m, passages))
    return cases

if __name__ == "__main__":
    main()