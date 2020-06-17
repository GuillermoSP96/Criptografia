import sys
import math
def euclides( m, n):
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    r0, r1 = m, n
    r, i = n, 2
    c = 0
    while r != 0:
        q = int(r0 / r1)
        x = x1 * q + x0
        y = y1 * q + y0
        res = r0 % r1
        print("{} = {} * {} + {}".format(int(r0), int(r1), int(q), int(res)))
        r = (math.pow(-1, i) * x * m) + (math.pow(-1, (i+1)) * y * n)
        i = i + 1
        x0, x1 = x1, x
        y0, y1 = y1, y
        r0, r1 = r1, r
        c = c + 1
    x = math.pow(-1, i) * x0
    y = math.pow(-1, i-1) * y0
    r = int(x * m + y * n)
    print("MCD({},{})={}".format(m, n, r))
    if y < 0:
        y2 = int(-1 * y)
        print("{}*{} - {}*{} = {}".format(int(x), int(m), int(y2), int(n),int(r)))
    else:
        print("{}*{} + {}*{} = {}".format(int(x), int(m), int(y), int(n),int(r)))
    print("Número de iteraciones = {}".format(c))
if __name__ == '__main__':
    euclides(int(sys.argv[1]), int(sys.argv[2]))
