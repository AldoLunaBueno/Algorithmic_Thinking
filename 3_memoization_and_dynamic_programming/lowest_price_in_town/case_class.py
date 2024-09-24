from typing import List

class Case:
    def __init__(self, nums: List[int], prices: List[float], desires: List[int]) -> None:
        self.nums = nums
        self.prices = prices
        self.desires = desires