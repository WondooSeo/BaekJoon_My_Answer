import sys

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().rstrip().split())
    bunja = 1; bunmo = 1;

    for i in range(N, K, -1):
        bunja *= i

    for j in range(1, N-K+1):
        bunmo *= j

    print(bunja//bunmo)
