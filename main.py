# square = [num**2 for num in range(1, 11)]
# print(square)
# def toSquares(firstNum, secondNum):
#     square = [num**2 for num in range(firstNum, secondNum)]
#     return square
# res = toSquares(1, 11)
# print(res)

# class Square:
#     def toSquares(self, firstNum, secondNum):
#         square = [num ** 2 for num in range(firstNum, secondNum)]
#         return square
# squareObj = Square()
# res = squareObj.toSquares(1, 11)
# print(res)

import math
class Square:
    def toSquares(self, firstNum, secondNum):
        square = [num ** 2 for num in range(firstNum, secondNum)]
        return square
    def squareRoots(self, nums):
        roots = [math.sqrt(num) for num in nums]
        return roots
squareObj = Square()
res = squareObj.toSquares(1, 11)
print(res)
roots = squareObj.squareRoots(res)
print(roots)