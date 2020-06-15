import sys
import  math
#a) (114160, 130002), (34036, 172611), (2154, 258577), (M 12 , M 24 ).
def euclides():
    m, n = 114160, 130002
    m, n = 34036, 172611
    m, n = 78105, 25030
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    r0, r1 = m, n
    r, i = n, 2
    # print("{} = {} * {} + {}".format(int(m), int(n), int(r0/r1), r0%r1))
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
    #(m, n) = xm + yn
    x = math.pow(-1, i) * x0
    y = math.pow(-1, i-1) * y0
    r = int(x * m + y * n)
    print("MCD({},{})={}".format(m, n, r))
    print("{}*{} + {}*{} = {}".format(int(x), int(m), int(y), int(n),int(r)))

if __name__ == '__main__':
    euclides()