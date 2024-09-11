from typing import List

# TIME: O(k * n**2), n:=number of days, k:=number of receipts per day
def solve_by_brute_force(receipts: List[List[int]]):
    total_prize = 0
    acc_receipts = []
    for day_receipts in receipts: # O(n) * O(n*k) = O(k * n**2 )
        acc_receipts.extend(day_receipts)
        minimum = min(acc_receipts) # O(n*k)
        maximum = max(acc_receipts) # O(n*k)
        acc_receipts.remove(minimum)
        acc_receipts.remove(maximum)
        prize = maximum - minimum
        total_prize += prize
    print(total_prize)