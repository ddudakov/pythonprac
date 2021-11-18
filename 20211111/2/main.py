class InvalidInput(Exception): pass
class BadTriangle(Exception): pass

def triangleSquare(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except Exception:
        raise InvalidInput
    try:    
        a = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
        b = ((x3-x2)**2 + (y3-y2)**2) ** 0.5
        c = ((x1-x3)**2 + (y1-y3)**2) ** 0.5
        p = (a+b+c)/2
        s = (p * (p-a) * (p-b) * (p-c)) ** 0.5
        1/s
    except (TypeError, ZeroDivisionError): 
        raise BadTriangle
    return s

while True:
    inStr = input()
    try:
        ans = triangleSquare(inStr)
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(f"{ans:.2f}")
        break
