# Problem: Food Lines
# Judge: dmoj
# ID: lkp18c2p1

def solve():
    line_1 = input() # N M
    line_2 = input() # N lines

    N, M = line_1.split(sep = " ")
    n_lines = line_2.split(sep = " ")
    N, M = int(N), int(M)
    n_lines = [int(line) for line in n_lines]

    for _ in range(M):
        min_idx, min_line = 0, float("inf")
        for i, line in enumerate(n_lines):
            if line < min_line:
                min_line = line
                min_idx = i
        print(str(n_lines[min_idx]))
        n_lines[min_idx] += 1