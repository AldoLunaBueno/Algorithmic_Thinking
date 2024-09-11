from heapq import heappush, heappop
from typing import List

def solve_using_heapq(receipts: List[List[int]]):
    total_prize = 0
    minheap: List[Receipt] = []
    maxheap: List[MaxHeapReceipt] = []
    for day_receipts in receipts:
        for receipt_cost in day_receipts:
            receipt = Receipt(receipt_cost)
            mh_receipt = MaxHeapReceipt(receipt)
            heappush(minheap, receipt)
            heappush(maxheap, mh_receipt)
        

        min_receipt: Receipt = None
        mhr_maximum: MaxHeapReceipt = None
        max_receipt: Receipt = None       
        
        while True:
            min_receipt = heappop(minheap)
            if min_receipt.is_used():
                continue
            min_receipt.use()
            break

        while True:
            mhr_maximum = heappop(maxheap)
            max_receipt = mhr_maximum.get_receipt()
            if max_receipt.is_used():
                continue
            max_receipt.use()
            break 

        prize = max_receipt.cost - min_receipt.cost
        total_prize += prize
    
    print(total_prize)
    
class Receipt:
    def __init__(self, cost):
        self.cost = cost
        self.used = False
    
    def is_used(self):
        return self.used
    
    def use(self):
        self.used = True
    
    def __lt__(self, other):
        return self.cost < other.cost
    
    def __eq__(self, other):
        return self.cost == other.cost


class MaxHeapReceipt:
    def __init__(self, receipt: Receipt):
        self._receipt = receipt
    
    def __lt__(self, other):
        return self._receipt.cost > other.get_receipt().cost
    
    def __eq__(self, other):
        return self._receipt.cost == other.get_receipt().cost
    
    def get_receipt(self):
        return self._receipt