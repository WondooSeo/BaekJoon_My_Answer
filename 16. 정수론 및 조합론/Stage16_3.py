import sys

if __name__ == '__main__':
    a, b = map(int, sys.stdin.readline().rstrip().split())
    a_t = a; b_t = b;
    while a_t != 0:
        b_t = b_t%a_t
        a_t, b_t = b_t, a_t

    gcd = b_t
    lcm = (a*b)//gcd
    print(gcd, lcm)
