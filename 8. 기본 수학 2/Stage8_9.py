import sys

if __name__ == '__main__':
    while True:
        A,B,C = map(int,sys.stdin.readline().rstrip().split())
        if A == 0 and B == 0 and C == 0:
            break
        byun = sorted([A,B,C])
        if byun[2]**2 == byun[0]**2+byun[1]**2:
            print('right')
        else:
            print('wrong')
