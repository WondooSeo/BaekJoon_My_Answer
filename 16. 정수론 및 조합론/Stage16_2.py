import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())

    real_yaksu = list(map(int,sys.stdin.readline().rstrip().split()))
    print(max(real_yaksu)*min(real_yaksu))
