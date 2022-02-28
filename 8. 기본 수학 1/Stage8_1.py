import sys

if __name__ == '__main__':
    A,B,C = map(int,sys.stdin.readline().rstrip().split())
    if B-C>=0:
        print(-1) 
    else:
        print(A//(C-B)+1)
