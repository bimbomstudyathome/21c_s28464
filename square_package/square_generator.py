import math
from abc import ABC, abstractmethod
class Square(ABC):
    @abstractmethod
    def toSquares(self, firstNum, secondNum):
        pass
    def squareRoots(self, nums):
        roots = [math.sqrt(num) for num in nums]
        return roots