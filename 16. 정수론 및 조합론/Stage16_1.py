import sys

if __name__ == '__main__':
    while True:
        a, b = map(int, sys.stdin.readline().rstrip().split())

        if (a, b) == (0, 0):
            break
        elif a%b == 0:
            print('multiple')
        elif b%a == 0:
            print('factor')
        else:
            print('neither')
