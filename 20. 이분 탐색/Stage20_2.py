import sys
from bisect import bisect_left, bisect_right

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    num_card = list(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline().rstrip())
    find_num = list(map(int, sys.stdin.readline().rstrip().split()))
    num_card.sort()

    for num in find_num:
        print(bisect_right(num_card, num) - bisect_left(num_card, num), end=' ')
