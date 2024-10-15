# Friends and Enemies (War)
# UVa problem 10158

from algorithms.my_way import solve

def main():
    num_people, operations = get_data()
    solve(num_people, operations)

def get_data():
    num_people = int(input())
    operations = []
    while True:
        op, x, y = [int(x) for x in input().split(" ")]
        if op == 0:
            break
        operations.append((op, x, y))
    return num_people, operations

if __name__ == "__main__":
    main()