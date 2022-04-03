import sys

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        A, B = map(int, sys.stdin.readline().rstrip().split())
        A, B = B, A
        lcm = A*B

    while A != 0:
        B = B%A
        A, B = B, A

    gcd = B
    print(lcm//gcd)
