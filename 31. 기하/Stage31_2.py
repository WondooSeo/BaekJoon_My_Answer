import sys


def ccw(point_list):
    v1 = [point_list[1][0] - point_list[0][0], point_list[1][1] - point_list[0][1]]
    v2 = [point_list[2][0] - point_list[1][0], point_list[2][1] - point_list[1][1]]
    return v1[0]*v2[1] - v1[1]*v2[0]


if __name__ == '__main__':
    point_list = list()
    for _ in range(3):
        point_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

    now_ccw = ccw(point_list)

    if now_ccw > 0:
        print(1)
    elif now_ccw < 0:
        print(-1)
    else:
        print(0)
