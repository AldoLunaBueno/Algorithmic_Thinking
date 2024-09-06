# Problem: Promotion
# Judge: SPOJ
# ID: PRO

from typing import List

def main():
    receipts = get_data()
    solve_by_brute_force(receipts)

def get_data() -> List[List[int]]:
    n = int(input())
    receipts = []
    for _ in range(n):
        line = input()
        k, *day_receipts = line.split(" ")
        day_receipts = [int(r) for r in day_receipts]
        receipts.append(day_receipts)
    return receipts

def solve_by_brute_force(receipts: List[List[int]]):
    total_prize = 0
    acc_receipts = []
    for day_receipts in receipts:
        acc_receipts.extend(day_receipts)
        minimum = min(acc_receipts)
        maximum = max(acc_receipts)
        acc_receipts.remove(minimum)
        acc_receipts.remove(maximum)
        prize = maximum - minimum
        total_prize += prize
    print(total_prize)

if __name__ == "__main__":
    main()