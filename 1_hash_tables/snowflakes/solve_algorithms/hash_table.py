from problem_constants import *
from typing import List
from comparator import Comparator

# TIME: O(n)
class HashTableAlgorithm:
    def __init__(self, comparator: Comparator):
        self.comparator = comparator
    
    def solve(self, n , n_lines):
        snowflakes: List[List] = [None] * MAX_SIZE
        for line in n_lines:
            code = sum(line) % MAX_SIZE # MAIN IDEA
            if snowflakes[code] == None:
                snowflakes[code] = [line]
            else:
                snowflakes[code].append(line)
        
        for snow_list in snowflakes: # time: O(a**2 * n/a) = O(n)
            if snow_list == None:
                continue
            a = len(snow_list)
            if a == 1:
                continue
            for i in range(a): # time: O(a**2)
                for j in range(i+1, a): # time: O(a)
                    # time: O(1), because ARMS = cte.
                    if self.comparator.identical(snow_list[i], snow_list[j]):
                        print(TWIN_MSG)
                        return
        print(NO_TWIN_MSG)