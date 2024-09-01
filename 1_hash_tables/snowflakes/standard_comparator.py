from problem_constants import *
from typing import List
from comparator import Comparator

class StandardComparator(Comparator):
    def identical(self, line_1: List, line_2: List) -> bool:
        """
        Returns True if lists are identical with some rotation clockwise (rigth) of counterclockwise (left)
        """
        for start in range(ARMS): # start for line_2
            if (self.identical_right(line_1, line_2, start) 
                or self.identical_left(line_1, line_2, start)):
                return True
        return False

    def identical_right(self, line_1, line_2, start):
        for offset in range(ARMS): # one by one arm
            if line_1[offset] != line_2[(start+offset) % ARMS]:
                return False # early verification
        return True

    def identical_left(self, line_1, line_2, start):
        for offset in range(ARMS): # one by one arm
            if line_1[offset] != line_2[start-offset]:
                return False # early verification
        return True