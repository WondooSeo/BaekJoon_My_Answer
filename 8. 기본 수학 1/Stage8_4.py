Simport sys
import math

if __name__ == '__main__':
    A,B,V = map(int,sys.stdin.readline().rstrip().split())
    print(math.ceil((V-A)/(A-B))+1)
