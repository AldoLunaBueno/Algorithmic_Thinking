from typing import List

def solved_using_own_heap(receipts: List[List[int]]):
    heap = MinHeap()
    heap.extract_min()
    pass


# min priority queue implementation

class MinHeap:
    def __init__(self, base_heap = []):
        self._heap = base_heap

    def insert(self, item):
        heap = self._heap
        heap.append(item)
        son = len(heap) - 1
        father = (son-1)//2
        while heap[son] < heap[father] and son != 0:
            heap[son], heap[father] = heap[father], heap[son]
            son = father
            father = (son-1)//2

    def extract_min(self):
        min_value = heap[0]
        
        # recovering min heap order property
        heap = self._heap
        father = 0
        heap[father] = heap.pop()
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
        
        return min_value

    def pushpop(self, item):
        self.insert(item)
        return self.extract_min()