import math
class Triangle():
    def __init__(self, sideA, sideB, sideC):
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC
    def countPerimeter(self):
        return self.sideA + self.sideB + self.sideC
    def countArea(self):
        p = (self.sideA + self.sideB + self.sideC)/2
        return math.sqrt(p*(p - self.sideA)*(p - self.sideB)*(p - self.sideC))
    #pass

class equilateral(Triangle):
    def __init__(self, side):
        self.sideA = side
        self.sideB = side
        self.sideC = side



inp = int(input())
oneSide = equilateral(inp)


print (oneSide.countArea())
print(oneSide.countPerimeter())