import sys
import math
def euclides( a, b):
    m, n = int(a), int(b)
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    r0, r1 = m, n
    r, i = n, 2
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
    x = math.pow(-1, i) * x0
    y = math.pow(-1, i-1) * y0
    r = int(x * m + y * n)
    print("MCD({},{})={}".format(m, n, r))
    print("{}*{} + {}*{} = {}".format(int(x), int(m), int(y), int(n),int(r)))

if __name__ == '__main__':
    euclides(sys.argv[1], sys.argv[2])