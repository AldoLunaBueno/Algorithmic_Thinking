# Problem: Snowflakes
# Judge: DMOJ 
# ID: cco07p2

def main():
    n, n_lines = get_data()
    solve(n, n_lines)

def get_data():
    n = int(input())
    n_lines = []
    for _ in range(n):
        line = input()
        line = line.split(" ")
        line = [int(x) for x in line]
        n_lines.append(line)
    return n, n_lines

def solve(n, n_lines):
    TWIN_MSG = "Twin snowflakes found."
    NO_TWIN_MSG = "No two snowflakes are alike."
    print(TWIN_MSG, end = "")

if __name__ == "__main__":
    main()