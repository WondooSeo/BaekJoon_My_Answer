import sys


def padoban(num):
    padoban_list = [1, 1, 1]
    if num > len(padoban_list):
        for i in range(len(padoban_list), num):
            padoban_list.append(padoban_list[i-2]+padoban_list[i-3])

    print(padoban_list[num-1])


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    for _ in range(N):
        padoban(int(sys.stdin.readline().rstrip()))
