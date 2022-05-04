def solveSquare(a, b, c):
    if a != 0:
        d = b**2 - 4*a*c
        if d < 0:
            return None
        else:
            x1 = (-b + d**0.5) / 2 / a
            x2 = (-b - d**0.5) / 2 / a
            return (min(x1, x2), max(x1, x2))
    else:
        if b!=0:
            return (-c/b, -c/b)
        else:
            return None if c!=0 else 'any value'

class SquareIO():

    def inputCoeff(self, name):
        return input(f"Input {name}: ")

    def printResult(self, result):
        print(f"Solution: {result}")


def solve():
    sio = SquareIO()
    a = sio.inputCoeff('a')
    b = sio.inputCoeff('b')
    c = sio.inputCoeff('c')
    sio.printResult(solveSquare(float(a), float(b), float(c)))
