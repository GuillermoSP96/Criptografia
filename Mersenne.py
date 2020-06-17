import sys
import math
def Mersenne(n):
    return int(math.pow(2,n)-1)
if __name__ == '__main__':
    print(Mersenne(int(sys.argv[1])))
