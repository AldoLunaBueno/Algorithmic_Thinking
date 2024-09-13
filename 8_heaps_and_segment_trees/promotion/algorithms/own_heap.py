from typing import List

MAX_RECEIPTS = 10**6

def solved_using_own_heap(receipts: List[List[int]]):
    minheap = MinHeap()
    maxheap = MinHeap()
    n = len(receipts)
    total_prize = 0
    used_list = [False] * MAX_RECEIPTS
    receipt_index = 0

    for i in range(n):

        day_receipts = receipts[i]
        could_be_used = []
        k = n-i
        
        if len(day_receipts) > 2*k:
            could_be_used_max = k_largest(day_receipts, k)
            could_be_used_min = k_smallest(day_receipts, k)

            for cost in could_be_used_min:
                receipt = Receipt(receipt_index, cost)
                minheap.push(receipt)
                receipt_index += 1

            for cost in could_be_used_max:
                receipt_neg = Receipt(receipt_index, -cost)
                maxheap.push(receipt_neg)
                receipt_index += 1

        else:
            could_be_used = day_receipts

            for cost in could_be_used:
                receipt = Receipt(receipt_index, cost)
                receipt_neg = Receipt(receipt_index, -cost)
                minheap.push(receipt)
                maxheap.push(receipt_neg)
                receipt_index += 1

        min_receipt: Receipt = None
        max_receipt: Receipt = None   

        min_receipt = minheap.pop()
        while used_list[min_receipt.get_index()]:
            min_receipt = minheap.pop()
        used_list[min_receipt.get_index()] = True

        max_receipt = maxheap.pop()
        while used_list[max_receipt.get_index()]:
            max_receipt = maxheap.pop()
        used_list[max_receipt.get_index()] = True

        prize = (-max_receipt.get_cost()) - min_receipt.get_cost()
        total_prize += prize
    
    print(total_prize)
    pass


class Receipt:
    def __init__(self, index: int, cost: int):
        self._index = index
        self._cost = cost

    def get_index(self):
        return self._index

    def get_cost(self):
        return self._cost
    
    def __lt__(self, other: "Receipt"):
        return self._cost < other.get_cost()

# min priority queue implementation

class MinHeap:
    def __init__(self, heap_arr: List = None):
        self._heap = heap_arr
        if heap_arr is None:
            self._heap = []
        
        self._heap

    def push(self, item):
        self._heap.append(item)
        self.heapify_up()

    def pop(self):
        heap = self._heap
        min_value = heap[0]
        heap[0] = heap.pop()
        self.heapify_down()
        return min_value

    def pushpop(self, item):
        heap = self._heap
        if heap and heap[0] < item:
            item, heap[0] = heap[0], item
            self.heapify_down()
        return item
    
    def heapify_up(self):
        """
        Recover min-heap-order property from bottom to top
        """
        heap = self._heap
        son = len(heap) - 1
        father = (son-1)//2
        while heap[son] < heap[father] and son != 0:
            heap[son], heap[father] = heap[father], heap[son]
            son = father
            father = (son-1)//2

    def heapify_down(self):
        """
        Recover min-heap-order property from top to bottom
        """
        heap = self._heap
        father = 0
        son_1, son_2 = 1, 2

        while True:
            next_son = None
            if son_2 < len(heap):
                next_son = son_1 if heap[son_1] < heap[son_2] else son_2
                if heap[next_son] < heap[father]:
                    heap[next_son], heap[father] = heap[father], heap[next_son]
                else:
                    break
            elif son_1 < len(heap):
                if heap[son_1] < heap[father]:
                    heap[son_1], heap[father] = heap[father], heap[son_1]
                break
            else:
                break

            father = next_son
            son_1 = 2 * father + 1
            son_2 = 2 * father + 2

    def get_heap(self):
        return self._heap
    
# extending operations

def k_largest(arr: List[int], k: int) -> List[int]:
    k_heap = MinHeap()

    # fill heap
    for i in range(0, k):
        k_heap.push(arr[i])

    # discart smallest
    for i in range(k, len(arr)):
        k_heap.pushpop(arr[i])

    return k_heap.get_heap()
    
def k_smallest(arr: List[int], k: int) -> List[int]:
    k_heap = MinHeap()

    # fill heap
    for i in range(0, k):
        k_heap.push(-arr[i])

    # discart smallest
    for i in range(k, len(arr)):
        k_heap.pushpop(-arr[i])
    
    return [-x for x in k_heap.get_heap()]