from square_package.square_generator import Square


class CubicGenerator(Square):
    def toCubes(self, firstNum, secondNum):
        if secondNum < firstNum:
            raise ValueError("Wrong range")
        cube = [num ** 3 for num in range(firstNum, secondNum)]
        return cube