from typing import List
from abc import ABC, abstractmethod

class Comparator(ABC):
    @abstractmethod
    def identical(self, line_1: List, line_2: List) -> bool:
        ...