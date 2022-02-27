import sys

if __name__ == '__main__':
    a = int(input())
    for _ in range(a):
        b,c = sys.stdin.readline().rstrip().split()
        c = list(c)
        for i in range(len(c)):
            print(c[i]*int(b),end='')
        print()
