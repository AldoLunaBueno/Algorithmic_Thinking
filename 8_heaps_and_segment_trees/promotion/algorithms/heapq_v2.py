from heapq import heappush, heappop, heappushpop
from typing import List

# The difference with v1 is "used" array
# apart from the Receipt objects

MAX_RECEIPTS = 10**6

def solve_using_heapq(receipts: List[List[int]]):
    n = len(receipts)
    total_prize = 0
    used = [False] * MAX_RECEIPTS
    receipt_index = 0
    minheap: List[Receipt] = []
    maxheap: List[Receipt] = []

    for i in range(n):

        day_receipts = receipts[i]
        could_be_used = []
        k = n-i
        if len(day_receipts) > 2*k:
            could_be_used = k_largest(day_receipts, k) + k_smallest(day_receipts, k)
        else:
            could_be_used = day_receipts


        for receipt_cost in could_be_used:
            receipt = Receipt(receipt_index, receipt_cost)
            receipt_neg = Receipt(receipt_index, -receipt_cost)
            heappush(minheap, receipt)
            heappush(maxheap, receipt_neg)
            receipt_index += 1

        min_receipt: Receipt = None
        max_receipt: Receipt = None   

        min_receipt = heappop(minheap)
        while used[min_receipt.get_index()]:
            min_receipt = heappop(minheap)
        used[min_receipt.get_index()] = True

        max_receipt = heappop(maxheap)
        while used[max_receipt.get_index()]:
            max_receipt = heappop(maxheap)
        used[max_receipt.get_index()] = True

        prize = (-max_receipt.get_cost()) - min_receipt.get_cost()
        total_prize += prize
    
    print(total_prize)
    
class Receipt:
    def __init__(self, index: int, cost: int):
        self._index = index
        self._cost = cost

    def get_index(self):
        return self._index

    def get_cost(self):
        return self._cost
    
    def __lt__(self, other):
        return self._cost < other.get_cost()
    
    def __eq__(self, other):
        return self._cost == other.get_cost()
    
def k_largest(arr: List[int], k: int) -> List[int]:
    k_heap = []

    # fill heap
    for i in range(0, k):
        heappush(k_heap, arr[i])

    # discart smallest
    for i in range(k, len(arr)):
        heappushpop(k_heap, arr[i])

    return k_heap
    
def k_smallest(arr: List[int], k: int) -> List[int]:
    k_heap = []

    # fill heap
    for i in range(0, k):
        heappush(k_heap, -arr[i])

    # discart smallest
    for i in range(k, len(arr)):
        heappushpop(k_heap, -arr[i])
    
    return [-x for x in k_heap]