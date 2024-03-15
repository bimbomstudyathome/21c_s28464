import math
class Square:
    def toSquares(self, firstNum, secondNum):
        if  secondNum < firstNum:
            raise ValueError("Wrong range")
        square = [num ** 2 for num in range(firstNum, secondNum)]
        return square
    def squareRoots(self, nums):
        roots = [math.sqrt(num) for num in nums]
        return roots