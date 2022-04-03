import sys

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().rstrip().split())
    bunja = 1; bunmo = 1;

    for i in range(1, K+1):
        bunmo *= i

    for j in range(N, N-K, -1):
        bunja *= j

    print((bunja//bunmo)%10007)
