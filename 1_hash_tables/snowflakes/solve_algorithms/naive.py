from problem_constants import *
from typing import List
from comparator import Comparator

# TIME: O(n**2)
class NaiveAlgorithm:
    def __init__(self, comparator: Comparator):
        self.comparator = comparator

    def solve(self, n, n_lines):
        for i in range(n): # time: O(n**2)
            for j in range(i+1, n): # time: O(n)
                # time: O(1), because ARMS = cte.
                if self.comparator.identical(n_lines[i], n_lines[j]):
                    print(TWIN_MSG)
                    return
        print(NO_TWIN_MSG)