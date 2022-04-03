import sys

if __name__ == '__main__':
    x, y, w, h = map(int, sys.stdin.readline().rstrip().split())
    wx = w-x; hy = h-y;
    print(min(x, y, wx, hy))
