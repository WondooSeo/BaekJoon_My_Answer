import sys


def gcd(a,b):
    while b > 0:
        a = a%b
        a, b = b, a

    return a


if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())
    wheel = list(map(int, sys.stdin.readline().rstrip().split()))

    for i in range(1, T):
        now_gcd = gcd(wheel[0], wheel[i])
        first_wheel = wheel[0] // now_gcd
        now_wheel = wheel[i] // now_gcd
        print(str(first_wheel)+'/'+str(now_wheel))
