from algorithms.my_way import solve

def main():
    target_height, jump, itching_powder = get_data()
    solve(target_height, jump, itching_powder)

def get_data():
    target_height, jump, n = [int(x) for x in input().split(" ")]
    itching_powder = []
    for _ in range(n):
        itching_powder.append([int(x) for x in input().split(" ")])
    return target_height, jump, itching_powder

if __name__ == "__main__":
    main()