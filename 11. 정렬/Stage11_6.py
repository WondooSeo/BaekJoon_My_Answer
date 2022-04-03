import sys

if __name__ == '__main__':
    N = int(input())
    point_list = list()

    for _ in range(N):
        point = list(map(int, sys.stdin.readline().rstrip().split()))
        point_list.append(point)

    point_list = sorted(point_list)

    for i in range(N):
        print(point_list[i][0], point_list[i][1])
